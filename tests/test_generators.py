from typing import Any

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(filter_descriptions_card_number: list) -> Any:
    """тестирование генератора filter_by_currency из файла generators"""
    generator = filter_by_currency(filter_descriptions_card_number)
    assert next(generator) == {
        "id": 939719571,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert next(generator) == 'в записи 594226728 нет поля "code" с описанием валюты'
    assert next(generator) == "пустая запись"


def test_transaction_descriptions(filter_descriptions_card_number: list) -> Any:
    """тестирование генератора transaction_descriptions из файла generators"""
    generator = transaction_descriptions(filter_descriptions_card_number)
    assert next(generator) == "Перевод организации"
    assert next(generator) == 'в записи 142264268 нет описания "description"'
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "пустая запись"


def test_card_number_generator() -> None:
    """тестирование генератора формирования номеров банковских карт"""

    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
