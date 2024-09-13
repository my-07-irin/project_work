import json

import requests

import os.path

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

    if not os.path.exists('../data/operations.json'):
        return new_operations
    else:
        with open('../data/operations.json', encoding="utf-8") as f:
            #data = json.load(f)
            #assert data == new_operations
            Mock.assert_called(json.load(f))
            Mock.assert_called_once(json.load(f))
        return True


if __name__ == '__main__':
    print(test_read_file())
# def test_path_file():
#     '''проверка наличия файла входных транзанкций'''
#     assert json.load(path_file='') == []
#     assert json.load(path_file='operations.json') == []
#     operations = json.load(path_file='../data/oper.json')
#     assert json.load(path_file='../data/oper.json') == operations
#     assert json.load(path_file='../data/oper1.json') == []
#     return
