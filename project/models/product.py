class Product:
    def __init__(self, name: str, category: str, price: float) -> None:
        if not name.strip():
            raise ValueError("name should not be empty")
        self.name = name
        self.edit_category(category)
        self.edit_price(price)
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        if not new_category.strip():
            raise ValueError("category should not be empty")
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        if (new_price < 0):
            raise ValueError(f"new_price should be non-negative, got: {new_price}")
        self.price = new_price

    def set_sale(self, sale: float) -> None:
        if (not 0 <= sale <= 100):
            raise ValueError(f"sale should be from 0 to 100, got {sale}")
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> float:
        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        return f"Product: name={self.name}, " \
                f"category={self.category}, price={self.price}, " \
                f"sale={self.sale}"
