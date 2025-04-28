from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
from urllib.parse import urljoin  # For URL joining

# Constants
AMAZON_BASE_URL = "https://www.amazon.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

def extract_product_title(soup):
    """Extract product title from soup object"""
    try:
        return soup.find("span", id="productTitle").text.strip()
    except AttributeError:
        return ""

def extract_product_rating(soup):
    """Extract product rating from soup object"""
    try:
        rating = soup.find("i", class_="a-icon-star").find_next("span").text.strip()
        return rating.split()[0]  # Get just the numeric part (e.g., "4.5" from "4.5 out of 5 stars")
    except (AttributeError, IndexError):
        return ""

def extract_review_count(soup):
    """Extract review count from soup object"""
    try:
        review_text = soup.find("span", id="acrCustomerReviewText").text.strip()
        return int(re.sub(r"[^\d]", "", review_text))  # Extract numeric part
    except (AttributeError, ValueError):
        return 0

def extract_availability(soup):
    """Extract availability status from soup object"""
    try:
        return soup.find("div", id="availability").find("span").text.strip()
    except AttributeError:
        return "Not Available"

def scrape_amazon_products(search_query, max_pages=1):
    """Main scraping function"""
    all_products = []
    
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        
        # Build search URL
        search_url = f"{AMAZON_BASE_URL}/s?k={search_query}&page={page}"
        
        try:
            response = requests.get(search_url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Get product links
            product_links = [
                urljoin(AMAZON_BASE_URL, link['href']) 
                for link in soup.select("a.a-link-normal.s-no-outline[href]")
                if '/dp/' in link['href']  # Only product pages
            ]
            
            # Scrape each product
            for product_url in product_links:
                try:
                    product_response = requests.get(product_url, headers=HEADERS, timeout=10)
                    product_response.raise_for_status()
                    product_soup = BeautifulSoup(product_response.content, "html.parser")
                    
                    product_data = {
                        "title": extract_product_title(product_soup),
                        "rating": extract_product_rating(product_soup),
                        "reviews": extract_review_count(product_soup),
                        "availability": extract_availability(product_soup),
                        "url": product_url
                    }
                    
                    if product_data["title"]:  # Only append if title exists
                        all_products.append(product_data)
                        
                    time.sleep(2)  # Be polite with delays
                    
                except Exception as e:
                    print(f"Error scraping product: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            continue
            
    return pd.DataFrame(all_products)

if __name__ == "__main__":
    # Example usage
    search_term = input("Enter product to search: ").strip().replace(" ", "+")
    max_pages = input("Enter the number of pages to scrape (default is 1): ").strip()
    max_pages = int(max_pages) if max_pages.isdigit() else 1

    products_df = scrape_amazon_products(search_term, max_pages=max_pages)
    
    if not products_df.empty:
        output_file = f"amazon_{search_term}_products.csv"
        products_df.to_csv(output_file, index=False)
        print(f"Success! Saved {len(products_df)} products to {output_file}")
    else:
        print("No products found or scraping failed.")
