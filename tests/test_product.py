from typing import Any


def test_init(product_init: Any) -> None:
    assert product_init.name == "Samsung Galaxy C23 Ultra"
    assert product_init.description == "256GB, Серый цвет, 200MP камера"
    assert product_init.price == 180000.0
    assert product_init.quantity == 5
