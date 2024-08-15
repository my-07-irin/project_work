from pathlib import Path
from time import time
from typing import Any, Callable
import os


def decorator_log(function: Callable) -> Callable:
    """декаратор автоматической регистрации деталей выполнения вызванной функции"""

    def wrapper(path_log: str) -> Any:
        """функция-оберка"""
        time_start = time()
        result = function(path_log)
        time_end = time()
        time_work = time_end - time_start
        if os.path.exists(path_log) is True:
            with open(f"{result}log.txt", "w", encoding="utf-8") as file:
                file.write(f"Вызвана функция: {function.__name__}   время работы функции: ")
                file.write(str(time_work))
        else:
            print(f"Вызвана функция:{function.__name__}")
            print(f"Время работы фукции: {time_work}")

        return function

    return wrapper


@decorator_log  # 'вызов декоратора'
def example(path_input: str) -> Any:
    for i in range(1000000):
        continue
    return path_input


#if __name__ == "__main__":
#    example("../data/")
#    example("")
#    example("../Dat/") #
