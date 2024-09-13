import csv

import numpy

import pandas as pd

import os


def get_spisok_from_csv(path_input: str) -> list:
    """формирование списка транзакций из файла формата csv"""

    transactions_from_csv: list = list()
    if os.path.exists(path_input) is False:
        return transactions_from_csv

    with open(path_input, "r", encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        for row in reader:
            transactions_row = {
                "id": row[0],
                "state": row[1],
                "date": row[2],
                "amount": row[3],
                "currency_name": row[4],
                "currency_code": row[5],
                "from": row[6],
                "to": row[7],
                "description": row[8],
            }
            transactions_from_csv.append(transactions_row)
    return transactions_from_csv


def get_spisok_from_excel(path_input: str) -> list:
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


if __name__ == "__main__":
    print(get_spisok_from_csv(""))
    #print(get_spisok_from_excel("../data/transactions_excel.xlsx"))
