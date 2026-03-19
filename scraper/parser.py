from bs4 import BeautifulSoup
from scraper.utils import clean_price, clean_rating, clean_availability

BASE_URL = "https://books.toscrape.com/catalogue/"


def parse_products(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    products = []

    items = soup.select("article.product_pod")

    for item in items:

        title = item.h3.a["title"]

        price_raw = item.select_one(".price_color").text
        rating_raw = item.select_one(".star-rating")["class"][1]
        availability_raw = item.select_one(".availability").text.strip()

        price = clean_price(price_raw)
        rating = clean_rating(rating_raw)
        availability = clean_availability(availability_raw)

        relative_url = item.h3.a["href"]
        product_url = BASE_URL + relative_url

        image_url = item.img["src"].replace("../..", "https://books.toscrape.com")

        products.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "product_url": product_url,
            "image_url": image_url
        })

    return products

def parse_product_detail(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    # descrição
    desc_tag = soup.select_one("#product_description + p")
    description = desc_tag.text.strip() if desc_tag else ""

    # categoria (breadcrumb)
    category = soup.select("ul.breadcrumb li a")[-1].text.strip()

    # UPC
    table = soup.select("table tr")
    upc = ""

    for row in table:
        header = row.select_one("th").text.strip()
        if header == "UPC":
            upc = row.select_one("td").text.strip()
            break

    return {
        "description": description,
        "category": category,
        "upc": upc
    }