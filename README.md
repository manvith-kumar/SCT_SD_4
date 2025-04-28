# SCT-SD_4: Amazon Product Scraper

## 🚀 Task Description
A Python web scraper that extracts product data (title, rating, reviews, availability) from Amazon search results and exports to CSV.

## ✨ Features
- **Search Any Product**: Enter any product name via CLI
- **Pagination Support**: Scrape multiple pages
- **Data Cleaning**: Normalized ratings and review counts
- **Polite Scraping**: Built-in delays between requests
- **CSV Export**: Structured output file

## 🛠️ Tech Stack
- Python 3.10+
- BeautifulSoup (HTML parsing)
- Requests (HTTP calls)
- Pandas (data export)

## 🏃‍♂️ How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the scraper:

   ```bash
   python amazon_scraper.py
3. Enter product name (e.g., wireless headphones)

4. View results in amazon_[product]_products.csv (e.g., amazon_wireless+earbuds_products)

## ⚠️ Ethical Note
- For educational purposes only

- Respect robots.txt and Amazon's terms

- Add delays (2+ sec) between requests

- Do not use for commercial scraping
