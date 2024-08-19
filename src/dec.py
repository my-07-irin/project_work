import os
from functools import wraps
from time import time
from typing import Any, Callable, Optional


def decorator_log(path_log: str) -> Callable:
    """декаратор автоматической регистрации деталей выполнения вызванной функции"""

    def inner(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_start = time()
            try:
                function(*args, **kwargs)
            except Exception:
                str_out = f"Функция: {function.__name__} error: {Exception} input: {args}, {kwargs}"
            else:
                time_end = time()
                time_work = time_end - time_start
                str_out = f"Функция: {function.__name__}   время работы функции: {time_work} "

            if os.path.exists(path_log) is True:
                with open(f"{path_log}log.txt", "w", encoding="utf-8") as file:
                    file.write(f"{str_out}")
            else:
                print(str_out)

            return

        return wrapper

    return inner


@decorator_log("../Data/")
def divining_numbers(a: float, b: float) -> float:
    """деление чисел с задержкой во времени"""
    for i in range(1000000):
        continue
    return a / b


if __name__ == "__main__":
    divining_numbers(10, 2)
#    help(divining_numbers)
