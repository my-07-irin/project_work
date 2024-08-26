from src.masks import get_mask_account, get_mask_card_number
from src.utils import read_file


def main() -> None:
    '''логирование приложений'''
    read_file("data/operations.json")
    get_mask_card_number("1234561234567845")
    get_mask_account("12345678901234567890")
    return
