import csv
import json


def export_csv(products: list, filename="data/products.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "title",
            "price",
            "rating",
            "availability",
            "product_url",
            "image_url",
            "description",
            "category",
            "upc"
        ])

        for p in products:
            writer.writerow([
                p["title"],
                p["price"],
                p["rating"],
                p["availability"],
                p["product_url"],
                p["image_url"],
                p["description"],
                p["category"],
                p["upc"]
            ])


def export_json(products: list, filename="data/products.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)