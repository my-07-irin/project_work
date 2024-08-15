import os
from functools import wraps
from time import time
from typing import Any, Callable, Optional


def decorator_log(path_log: Optional[str] = None) -> Callable:
    """декаратор автоматической регистрации деталей выполнения вызванной функции"""

    def inner(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_start = time()
            result = function(*args, **kwargs)
            time_end = time()
            time_work = time_end - time_start
            if os.path.exists(*args, **kwargs) is True:
                with open(f"{result}log.txt", "w", encoding="utf-8") as file:
                    file.write(f"Вызвана функция: {function.__name__}   время работы функции: ")
                    file.write(str(time_work))
            else:
                print(f"Вызвана функция:{function.__name__}")
                print(f"Время работы фукции: {time_work}")

            return result

        return wrapper

    return inner


@decorator_log("../Data/")
def example(path_input: str) -> Any:
    """функция перебора чисел из заданного диапазона"""
    for i in range(1000000):
        continue
    return path_input


#if __name__ == "__main__":
#    example("../data/")
#    example("")
#    example("../Dat/") #
#    help(example)
