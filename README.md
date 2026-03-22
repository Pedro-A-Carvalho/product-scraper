# Product Scraper (Async Python)

A professional asynchronous product scraper built with Python.

This project simulates real-world freelance scraping tasks, extracting structured product data from an e-commerce-like website.

---

## Features

- Async scraping with aiohttp
- Concurrency control using asyncio.Semaphore
- Retry with exponential backoff
- User-Agent rotation
- Multi-level scraping (list page → product page)
- Data normalization (price, rating, availability)
- CSV and JSON export
- Progress bar with tqdm
- Failed URL tracking
- CLI arguments support

---

## Data Collected

Each product includes:

- Title
- Price (float)
- Rating (int)
- Availability (boolean)
- Product URL
- Image URL
- Description
- Category
- UPC

---

## Project Structure
```
product-scraper/
│
├── scraper/
│   ├── fetcher.py
│   ├── parser.py
│   ├── exporter.py
│   └── utils.py
│
├── data/
│   ├── products.csv
│   ├── products.json
│   └── failed_urls.txt
│
├── main.py
├── requirements.txt
└── README.md
```
---

## Installation
```
git clone https://github.com/YOUR_USERNAME/product-scraper.git

cd product-scraper
x
python -m venv venv
x
source venv/bin/activate
x
pip install -r requirements.txt
```
---

## Usage

Run the scraper:
```
python main.py
```
Custom options:
```
python main.py --url https://books.toscrape.com/catalogue/page-1.html --concurrency 10
```
---

## Output

The scraper generates:

data/products.csv
data/products.json
data/failed_urls.txt (if any failures occur)

---

## Example Output

title,price,rating,availability,category
A Light in the Attic,51.77,3,True,Poetry

---

## Technologies Used

- Python
- asyncio
- aiohttp
- BeautifulSoup
- tqdm

---

## Notes

This project is for educational purposes only.
The target website is designed for scraping practice.