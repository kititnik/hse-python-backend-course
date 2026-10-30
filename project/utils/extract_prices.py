from models.product import Product


def extract_prices(products: list[Product]) -> list[float]:
    prices = []
    for product in products:
        prices.append(product.get_price())
    return prices
