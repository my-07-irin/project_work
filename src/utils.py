import json

import requests

def read_file(path_file: str):
    '''чтение транзакций из json файла'''
    new_operations = []
    with open(path_file, encoding='utf-8') as f:
        data = json.load(f)

        if data == [] or type(data) != type(new_operations):
            return new_operations
        for info_list in data:
            if info_list != {}:
                if info_list["operationAmount"]["currency"]["code"] == 'RUB':
                    new_operations.append(info_list)
        print(new_operations)

    return new_operations

if __name__ == '__main__':
    read_file('../data/operations.json')