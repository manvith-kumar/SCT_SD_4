import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_amazon_products(search_query, max_pages=1):
    """Scrape product data from Amazon search results."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    products = []
    
    for page in range(1, max_pages + 1):
        url = f"https://www.amazon.in/s?k={search_query}&page={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for item in soup.select('.s-result-item'):
            try:
                name = item.select_one('h2 a span').text.strip()
                price = item.select_one('.a-price-whole').text.replace(',', '').strip()
                rating = item.select_one('.a-icon-alt').text.split()[0]
                products.append([name, price, rating])
            except AttributeError:
                continue
        
        time.sleep(2)  # Be polite with requests
    
    return products

def save_to_csv(data, filename):
    """Save scraped data to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price (₹)', 'Rating'])
        writer.writerows(data)

if __name__ == "__main__":
    search_term = input("Enter product to search: ")
    products = scrape_amazon_products(search_term)
    
    if products:
        save_to_csv(products, 'products.csv')
        print(f"Successfully scraped {len(products)} products. Data saved to products.csv")
    else:
        print("No products found or scraping failed.")
