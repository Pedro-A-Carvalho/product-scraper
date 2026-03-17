import csv


def export_products(products: list, filename="data/products.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "title",
            "price",
            "rating",
            "availability",
            "product_url",
            "image_url"
        ])

        for p in products:
            writer.writerow([
                p["title"],
                p["price"],
                p["rating"],
                p["availability"],
                p["product_url"],
                p["image_url"]
            ])