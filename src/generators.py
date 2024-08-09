from typing import Any


def filter_by_currency(list_input: list, currency_input: str = "USD") -> Any:
    """транзакции по заданному коду валюты"""

    if list_input == []:
        print("транзакции по кодам валют: нет данных, список пустой")
        return

    for info_list in list_input:
        if info_list == {}:
            yield "пустая запись"
        else:
            try:
                if info_list["operationAmount"]["currency"]["code"] == currency_input:
                    yield info_list
            except KeyError:
                yield (f'в записи {info_list.get("id")} нет поля "code" с описанием валюты')


def transaction_descriptions(list_input: list) -> Any:
    """транзакции по видам операций"""

    if list_input == []:
        print("транзакции по видам операций: нет данных, список пустой")
        return

    for info_operation in list_input:
        if info_operation == {}:
            yield "пустая запись"
        elif info_operation.get("description") is None:
            yield f'в записи {info_operation.get("id")} нет описания "description"'
        else:
            yield info_operation.get("description")


def card_number_generator(start_input: int, end_input: int) -> Any:
    """генератор формирования номеров банковских карт"""
    if start_input < 1 or end_input < 1 or end_input < start_input:
        return print("Неправильный ввод чисел для формирования номера карты")
    for number in range(start_input, end_input + 1):
        count_length = 1
        new_string = ""

        while count_length <= 16 - len(str(number)):
            new_string += "0"
            count_length += 1

        new_string = f"{new_string}{str(number)}"
        card_number = f"{new_string[0:4]} {new_string[4:8]} {new_string[8:12]} {new_string[12:]}"
        yield card_number


# if __name__ == "__main__":
#     list_bank = [
#         {
#             "id": 939719571,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229",
#         },
#         {
#             "id": 594226729,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#         {
#             "id": 594226728,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                 },
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#         {},
#     ]
#
#     usd_transactions = filter_by_currency(list_bank)
#
#     for info_list in usd_transactions:
#         print(info_list)
#
#     description_operation = transaction_descriptions(list_bank)
#
#     for operation_out in description_operation:
#         print(operation_out)
#
#     number_card = card_number_generator(9999999999999998, 10000000000000000)
#     for card_number in number_card:
#         print(card_number)
