import json
import os
from src.category import Category
from src.product import Product

def read_file(path_input: str) -> dict:
    full_path = os.path.abspath(path_input)
    with open(full_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def create_object_category_product(data):
    category_from_file = []
    for category in data:
        products_from_file = []
        for product in category["products"]:
            products_from_file.append(Product(**product))
        category_from_file.append(Category(**category))

    return category_from_file



if __name__ == "__main__":
    data_from_file = read_file("../data/products.json")
    category_s = create_object_category_product(data_from_file)
    print(category_s)

    print(category_s[0].name)
    print(category_s[0].description)
    print(category_s[0].products)
