import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_init():
    return (Category
                ("Смартфоны", "Смартфоны, как средство не только коммуникации",

                [
                             {
                               "name": "Samsung Galaxy C23 Ultra",
                               "description": "256GB, Серый цвет, 200MP камера",
                               "price": 180000.0,
                               "quantity": 5
                             },
                             {
                               "name": "Iphone 15",
                               "description": "512GB, Gray space",
                               "price": 210000.0,
                               "quantity": 8
                             },
                             {
                               "name": "Xiaomi Redmi Note 11",
                               "description": "1024GB, Синий",
                               "price": 31000.0,
                               "quantity": 14
                             }
                         ]
                ))

@pytest.fixture
def product_init():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)





