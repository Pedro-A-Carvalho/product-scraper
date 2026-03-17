import asyncio

from scraper.fetcher import fetch_html
from scraper.parser import parse_products
from scraper.exporter import export_products


URL = "https://books.toscrape.com/catalogue/page-1.html"


async def main():
    html = await fetch_html(URL)

    products = parse_products(html)

    export_products(products)

    print(f"Scraped {len(products)} products")


if __name__ == "__main__":
    asyncio.run(main())