import os

import json

from dotenv import load_dotenv

import requests

load_dotenv()

def conversion_currency(path_file):

    API_KEY = os.getenv('API_KEY')
    headers = {
        "apikey": f'{API_KEY}'
    }

    ur1 = "https://api.apilayer.com/exchangerates_data/convert"
    new_operations = []
    with open(path_file, encoding='utf-8') as f:
        data = json.load(f)
        if data == [] or type(data) != type(new_operations):
            return new_operations

        for info_list in data:
            if info_list != {}:
                if info_list["operationAmount"]["currency"]["code"] == "RUB":
                    new_operations.append(info_list)
                else:
                    code_from_file = info_list["operationAmount"]["currency"]["code"]
                    amount_from_file =info_list["operationAmount"]["amount"]

                    payload = {
                        "amount": f'{amount_from_file}',
                        "from": f'{code_from_file}',
                        "to": "RUB"
                    }
                    response = requests.get(ur1, params=payload, headers=headers)
                    repos = response.json()
                    print(repos)
                    resul = repos["result"]

                    info_list["operationAmount"]["currency"]["code"] = "RUB"
                    info_list["operationAmount"]["currency"]["name"] = "руб."
                    info_list["operationAmount"]["amount"] = repos["result"]
                    new_operations.append(info_list)
                    #print(info_list)
                    new_operations.append(info_list)

    return new_operations


if __name__ == '__main__':
     conversion_currency('../data/operations.json')

#     # status_code = response.status_code
#     # print(f"Статус код: {status_code}")

