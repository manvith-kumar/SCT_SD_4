# SCT_SD_4 - E-commerce Web Scraper

## 📝 Task Description
Create a Python program that extracts product information (name, price, rating) from e-commerce websites and stores it in a CSV file.

## ✨ Features
- Scrapes product data from Amazon search results
- Handles pagination (multiple pages)
- Saves data to structured CSV format
- Implements polite scraping with delays between requests
- Error handling for robust operation

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
2. **Run the scraper**:
   ```bash
   python ecommerce_scraper.py

3. **Enter a product name** when prompted (e.g., "wireless headphones")

4. **View results** in products.csv

## Tech Stack
- Python 3.x
- BeautifulSoup (HTML parsing)
- Requests (HTTP calls)
- CSV (data export)

## Example Output (products.csv)
   ```bash
   Product Name,Price (₹),Rating
   boAt Airdopes 141,1299,4.1
   JBL Tune 230NC,5999,4.3
   Sony WH-CH720N,7990,4.2
   ```
   
## Ethical Note
- This is for educational purposes only
- Respect websites' robots.txt and terms of service
- Add delays between requests to avoid overloading servers
