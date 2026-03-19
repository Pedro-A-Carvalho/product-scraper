import asyncio

from scraper.exporter import export_products
from scraper.fetcher import fetch_html, fetch_multiple
from scraper.parser import parse_products, parse_product_detail


URL = "https://books.toscrape.com/catalogue/page-1.html"


async def main():
    html = await fetch_html(URL)

    products = parse_products(html)

    # pegar links dos produtos
    product_urls = [p["product_url"] for p in products]

    # buscar páginas dos produtos
    product_pages = await fetch_multiple(product_urls)

    # extrair detalhes
    for product, page_html in zip(products, product_pages):
        details = parse_product_detail(page_html)
        product.update(details)

    export_products(products)

    print(f"Scraped {len(products)} products with details")


if __name__ == "__main__":
    asyncio.run(main())