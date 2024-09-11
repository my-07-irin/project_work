from src.masks import get_mask_account, get_mask_card_number
from src.utils import read_file
from src.category import Category
from src.product import Product
from src.read_from_file_product import open_read_file, create_object_category_product


def main() -> None:
    '''логирование приложений'''
    read_file("data/operations.json")
    get_mask_card_number("1234561234567845")
    get_mask_account("12345678901234567890")

    create_object_category_product(open_read_file("/data/products.json"))
    return
