import json

import requests

import os


from dotenv import load_dotenv

load_dotenv()


def conversion_currency(path_file: str) -> list:
    """конвертация валюты в транзакциях"""

    API_KEY = os.getenv("API_KEY")
    headers = {"apikey": f"{API_KEY}"}

    ur1 = "https://api.apilayer.com/exchangerates_data/convert"
    new_operations = []

    with open(path_file, encoding="utf-8") as f:
        data = json.load(f)
        if data == [] or type(data) is not type(new_operations):
            return new_operations

    for info_list in data:
        if info_list != {}:
            if info_list["operationAmount"]["currency"]["code"] == "RUB":
                new_operations.append(info_list)
            else:
                code_from_file = info_list["operationAmount"]["currency"]["code"]
                amount_from_file = info_list["operationAmount"]["amount"]
                payload = {"amount": f"{amount_from_file}", "from": f"{code_from_file}", "to": "RUB"}
                response = requests.get(ur1, params=payload, headers=headers)
                repos = response.json()

                info_list["operationAmount"]["currency"]["code"] = "RUB"
                info_list["operationAmount"]["currency"]["name"] = "руб."
                info_list["operationAmount"]["amount"] = repos["result"]
                new_operations.append(info_list)
                new_operations.append(info_list)

    return new_operations
