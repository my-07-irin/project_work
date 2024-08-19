card_number_input: str
account_number_input: str

def get_mask_card_number(cart_number: str) -> str:
    """маскировка введенного номера банковской карты"""

    if len(cart_number) >= 16 and cart_number.isdigit():
        number_card = f"{cart_number[0:4]} {cart_number[4:6]}** **** {cart_number[12:16]}"
    elif cart_number == '':
        number_card = ''
    else:
        number_card = "номер карты введён неверно"

    return number_card


def get_mask_account(account: str) -> str:
    """маскировка введенного номера банковского счёта"""
    if len(account) >= 4 and account.isdigit():
        number_account = f"**{account[-4:]}"
    elif account == '':
        number_account = ''
    else:
        number_account = "номер счёта введён неверно"

    return number_account


# if __name__ == "__main__":
#     card_number_input = input("Введите номер карты в формате XXXXXXХХХХХХXXХХ: ")
#     print(get_mask_card_number(card_number_input))
#
#     account_number_input = input("Введите номер счёта в формате XXXXXXХХХХХХXXХХХХХХ: ")
#     print(get_mask_account(account_number_input))
