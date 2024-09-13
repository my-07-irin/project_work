class Product:
    """создание класса продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """инициализация класса продукт"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":

    product_s = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет 200MP, камера", 180000.0, 5)

    print(product_s.name)
    print(product_s.description)
    print(product_s.price)
    print(product_s.quantity)
