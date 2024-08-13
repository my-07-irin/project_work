def mask_account_card(card_or_account: str) -> str:
    """проверка ввода типа и номера карты или номера счета"""

    card_account_input = []
    text_output = ""

    if card_or_account == "":
        text_output = ""
    else:
        card_account_input = card_or_account.split(" ")
        if card_account_input[0].lower() == "счет" or card_account_input[0].lower() == "счёт":
            if card_account_input[1].isdigit() and len(card_account_input[1]) >= 4:
                text_output += f"Счет **{card_account_input[1][-4:]}"
            else:
                text_output += f"Неправильный набор цифр счета {card_account_input[1]}"
        else:
            if not card_account_input[0].isalpha():
                text_output = "не выбран тип карты"
                return text_output

            text_output = ""

            for text in card_account_input:
                if text.isalpha():
                    text_output += f"{text} "
                else:
                    if text.isdigit() and len(text) >= 16:
                        text_output += f"{text[0:4]} {text[4:6]}** **** {text[12:16]}"
                    else:
                        text_output += f"Неправильный набор цифр карты {text[0:4]}"
    return text_output


def get_date(my_date: str) -> str:
    """перевод введенной даты в формат ГГГГ.ММ.ДД"""

    if my_date == "":
        string_date = ""
    elif len(my_date) < 10:
        string_date = "дата введена неверно"
    else:
        string_date = f"{my_date[8:10]}.{my_date[5:7]}.{my_date[0:4]}"

    return string_date


# if __name__ == '__main__':
#     assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
#     card_or_account_input = input("Вввдите тип и номер карты в формате: тип XXXXXXXXXXXXXXXX или \
#     введите номер счета в формате: Счет XXXXXXXXXXXXXXXXXXXX: ")
#     card_or_account_out = mask_account_card(card_or_account_input)
#     print(card_or_account_out)
#
#     date_time = input("Введите дату в формате ГГГГ-ММ-ДДТЧЧ:ММ:СС ХХХХХХ ")
#     print(get_date(date_time))