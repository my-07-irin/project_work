from unittest.mock import Mock

from unittest.mock import patch

import pandas as pd

import numpy

import os

from pathlib import Path

from src.read_from_files import get_spisok_from_csv


def test_get_spisok_from_csv() -> list:
    mock_transactions_from_cvs = Mock(return_value=
    [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }
    ])
    transactions_from_cvs = mock_transactions_from_cvs
    assert get_spisok_from_csv('..data/transactions.csv') == [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }
    ]
    mock_transactions_from_cvs.assert_called_once('..data/transactions.csv')
    mock_transactions_from_cvs.assert_called('..data/transactions.csv')

    return


def get_spisok_from_excel(path_input='') -> list:
    """формирование списка транзакций из файла формата excel"""

    # создание пустого списка, пустого справочника, списка наименований ключей транзакций, счетчика
    transactions_spis: list = list()
    transactions_row = {}
    name_col = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
    count = 0

    transactions_from_excel = pd.read_excel(path_input)    #, sheet_name="Лист 1"
    count_row = transactions_from_excel.shape[0]  # кол-во записей

    while count < count_row:
        for i in range(9):
            if i == 0:
                transactions_row[name_col[i]] = int(numpy.nan_to_num(transactions_from_excel.iloc[count, i]))
            elif i == 3:
                transactions_row[name_col[i]] = int(numpy.nan_to_num(transactions_from_excel.iloc[count, i]))
            else:
                transactions_row[name_col[i]] = transactions_from_excel.iloc[count, i]

        transactions_spis.append(transactions_row)
        transactions_row = {}
        count += 1

    return transactions_spis







