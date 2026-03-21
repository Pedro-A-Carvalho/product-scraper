import asyncio
import aiohttp
import argparse
from scraper.exporter import export_csv, export_json
from scraper.fetcher import fetch, fetch_multiple
from scraper.parser import parse_products, parse_product_detail


URL = "https://books.toscrape.com/catalogue/page-1.html"

def parse_args():
    parser = argparse.ArgumentParser(description="Product Scraper")

    parser.add_argument("--url", type=str, default=URL)
    parser.add_argument("--concurrency", type=int, default=5)

    return parser.parse_args()


async def main():
    args = parse_args()

    url = args.url
    concurrency = args.concurrency

    semaphore = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,URL,semaphore)

        products = parse_products(html)

        # pegar links dos produtos
        product_urls = [p["product_url"] for p in products]

        # buscar páginas dos produtos
        product_pages = await fetch_multiple(session, product_urls)

        # extrair detalhes
        for product, page_html in zip(products, product_pages):

            if not page_html:
                continue

            details = parse_product_detail(page_html)

            product.update(details)

        export_csv(products)
        export_json(products)

    print(f"Scraped {len(products)} products with details")


if __name__ == "__main__":
    asyncio.run(main())