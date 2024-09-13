import logging

card_number_input: str
account_number_input: str

# создание логера, хендлера, формата
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

# установка логера, форматтера, хендлера, уровня логера
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(cart_number: str) -> str:
    """маскировка введенного номера банковской карты"""

    if len(cart_number) >= 16 and cart_number.isdigit():
        number_card = f"{cart_number[0:4]} {cart_number[4:6]}** **** {cart_number[12:16]}"
        logger.info("Номер введенной карты удачно отформатирован")
    elif cart_number == "":
        number_card = ""
        logger.warning("Номер карты не введен")
    else:
        number_card = "номер карты введён неверно"
        logger.error("Номер карты введен неправильно")
    logger.info("Приложение закончило работу")
    return number_card


def get_mask_account(account: str) -> str:
    """маскировка введенного номера банковского счёта"""
    if len(account) >= 4 and account.isdigit():
        number_account = f"**{account[-4:]}"
        logger.info("Сформирован отформатированный номер счета")
    elif account == "":
        number_account = ""
        logger.warning("Не введен номер счета")
    else:
        number_account = "номер счёта введён неверно"
        logger.error("номер счета введен неверно")
    logger.info("Приложение закончило работу")
    return number_account


# if __name__ == "__main__":
#     card_number_input = input("Введите номер карты в формате XXXXXXХХХХХХXXХХ: ")
#     print(get_mask_card_number(card_number_input))
#
#     account_number_input = input("Введите номер счёта в формате XXXXXXХХХХХХXXХХХХХХ: ")
#     print(get_mask_account(account_number_input))
