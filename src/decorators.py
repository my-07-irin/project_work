from functools import wraps
from typing import Any, Callable


def decorator_log(path_log: Any = None) -> Any:
    """декаратор автоматической регистрации деталей выполнения вызванной функции"""

    def inner(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                str_out = f"Функция: {function.__name__} error: {e} input: {args}, {kwargs}"
                result = None
            else:
                str_out = f"Функция: {function.__name__} OK "
                result = function(*args, **kwargs)
            if path_log is not None:
                with open(f"{path_log}", "w", encoding="utf-8") as file:
                    file.write(f"{str_out}")
            else:
                print(str_out)
            return result

        return wrapper

    return inner


@decorator_log(path_log="../data/log.txt")
def divining_numbers(a: int, b: int) -> float:
    """деление чисел с задержкой во времени"""
    for i in range(1000000):
        continue
    return a / b
