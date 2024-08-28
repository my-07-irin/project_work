import json
import logging
import os.path

# создание логера, хендлера, формата
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

# установка логера, форматтера, хендлера, уровня логера
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_file(path_file: str) -> list:
    """чтение транзакций из json файла"""
    new_operations: list = list()
    if not os.path.exists(path_file):
        logger.warning("Файд входных данных не найден")
        logger.info("Приложение закончило работу в связи с отсутствием водного файла")
        return new_operations
    with open(path_file, encoding="utf-8") as f:
        data = json.load(f)
    logger.info("Файл входных данных открыт и преобразован в формат Python")
    if data == [] or type(data) is not type(new_operations):
        logger.warning("Файл входных данных пустой")
        return new_operations
    for info_list in data:
        if info_list != {}:
            new_operations.append(info_list)
    if not new_operations == []:
        logger.info("Успешно создан список транзакций. Приложение закончило работу")
    return new_operations
