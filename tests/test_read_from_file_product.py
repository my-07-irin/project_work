import json
import os
from src.read_from_file_product import open_read_file
from src.read_from_file_product import create_object_category_product


def test_open_file():
    if os.path.exists(os.path.abspath("../data/products.json")):
        with open("../data/products.json", 'r', encoding='UTF-8') as f:
            data_test = json.load(f)

    result = open_read_file("../data/products.json")
    result_object = create_object_category_product(result)
    result_test_object = create_object_category_product(data_test)

    assert data_test == result

    assert result_test_object[0].name == result_object[0].name
    assert result_test_object[0].description == result_object[0].description
    assert result_test_object[0].products == result_object[0].products
