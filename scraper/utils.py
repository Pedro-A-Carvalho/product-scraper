def clean_price(price_str: str) -> float:
    price_str = price_str.replace("£", "").replace("Â", "")
    return float(price_str)


def clean_rating(rating_str: str) -> int:
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return mapping.get(rating_str, 0)


def clean_availability(text: str) -> bool:
    return "In stock" in text