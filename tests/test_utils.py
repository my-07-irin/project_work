import json

import requests

from unittest.mock import Mock

from unittest.mock import patch

from src.utils import read_file


def test_read_file():

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

    assert read_file('../data/operations.json') == new_operations
    Mock.assert_called(read_file('../data/operations.json'))
    Mock.assert_called_once(read_file('../data/operations.json'))

    return


def test_path_file():
    '''проверка наличия файла входных транзанкций'''
    assert read_file(path_file='') == []
    assert read_file(path_file='operations.json') == []
    operations = read_file(path_file='../data/oper.json')
    assert read_file(path_file='../data/oper.json') == operations
    assert read_file(path_file='../data/oper1.json') == []
    return
