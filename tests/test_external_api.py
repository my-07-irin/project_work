import json

import requests

from unittest.mock import Mock

from unittest.mock import patch

from src.external_api import conversion_currency
def test_conversion_currency():

    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
    ]

    mock_new_operations = Mock(return_value=operations)
    new_operations = mock_new_operations


    assert conversion_currency('../data/operations.json') == new_operations
    Mock.assert_called(conversion_currency('../data/operations.json'))
    Mock.assert_called_once(conversion_currency('../data/operations.json'))

    return


def test_path_file():
    '''проверка наличия файла входных транзанкций'''
    assert conversion_currency(path_file='') == []
    assert conversion_currency(path_file='operations.json') == []
    operations = conversion_currency(path_file='../data/oper.json')
    assert conversion_currency(path_file='../data/oper.json') == operations
    return

