def mask_account_card(card_or_account: str) -> str:
    """проверка ввода типа и номера карты или номера счета"""

    card_account_input = []
    text_output = ""

    card_account_input = card_or_account.split(" ")
    if card_account_input[0].lower() == "счет" or card_account_input[0].lower() == "счёт":
        if card_account_input[1].isdigit() and len(card_account_input[1]) == 20:
            text_output += f"Счет **{card_account_input[1][16:]}"
        else:
            text_output += f"Неправильный набор цифр счета {card_account_input[1]}"
    else:
        text_output = ""

        for text in card_account_input:
            if text.isalpha():
                text_output += f"{text} "
            else:
                if text.isdigit() and len(text) == 16:
                    text_output += f"{text[0:4]} ** **** {text[12:]}"
                else:
                    text_output += f"Неправильный набор цифр карты {text[0:4]}"
    return text_output


def get_date(my_date: str) -> str:
    """перевод введенной даты в формат ГГГГ.ММ.ДД"""

    string_date = f"{my_date[8:10]}.{my_date[5:7]}.{my_date[0:4]}"

    return string_date


print("Вввдите тип и номер карты в формате: тип XXXXXXXXXXXXXXXX")

card_or_account_input = input("или введите номер счета в формате: Счет XXXXXXXXXXXXXXXXXXXX: ")
print(mask_account_card(card_or_account_input))

date_time = input("Введите дату в формате ГГГГ-ММ-ДДТЧЧ:ММ:СС ХХХХХХ ")
print(get_date(date_time))
