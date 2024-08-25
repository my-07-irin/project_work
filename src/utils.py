import json
import os.path


def read_file(path_file: str) -> list:
    """чтение транзакций из json файла"""
    new_operations = []
    if path_file is None or os.path.exists(path_file) is False:
        return new_operations
    with open(path_file, encoding="utf-8") as f:
        data = json.load(f)

    if data == [] or type(data) is not type(new_operations):
        return new_operations
    for info_list in data:
        if info_list != {}:
            new_operations.append(info_list)

    return new_operations
