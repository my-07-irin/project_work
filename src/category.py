from src.product import Product


class Category:
    """Создание класса категория продукта"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """инициализация класса категория продукта"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 10000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category_s = Category(
        "Смартфоны", "Смартфоны, как средство не только коммуникации", [product_1, product_2, product_3]
    )

    print(category_s.name)
    print(category_s.description)
    print(category_s.products)
    print(category_s.category_count)
    print(category_s.product_count)
