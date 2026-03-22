import asyncio
import aiohttp
import argparse
from tqdm import tqdm
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

        product_urls = [p["product_url"] for p in products]

        product_pages = await fetch_multiple(session, product_urls)

        failed_urls = []

        for product, page_html in tqdm(
            zip(products, product_pages),
            total=len(products),
            desc="Scraping product details"
        ):

            if not page_html:
                failed_urls.append(product["product_url"])
                continue

            details = parse_product_detail(page_html)

            product.update(details)

        export_csv(products)
        export_json(products)

        if failed_urls:
            with open("data/failed_urls.txt", "w") as f:
                for url in failed_urls:
                    f.write(url + "\n")

    print(f"Scraped {len(products)} products with details")


if __name__ == "__main__":
    asyncio.run(main())