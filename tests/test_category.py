from src.category import Category


def test_init(category_init) -> None:
    Category.category_count = 0
    Category.product_count = 0
    assert category_init.name == "Смартфоны"
    assert category_init.description == "Смартфоны, как средство не только коммуникации"
    assert category_init.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]


def test_count_category_product(category_init) -> None:

    assert category_init.category_count == 1
    assert category_init.product_count == 3
