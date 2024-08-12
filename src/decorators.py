from time import time


from typing import Callable


def decorator_log(predicate, error_message):
    """логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def wrapper(function):
        def inner(arg):
            time_start = time()
            result = function(arg)
            time_end = time()
            time_work = time_end - time_start
            if predicate(arg):
                try:
                    with open(arg, 'w', encoding='utf-8') as file:
                         file.write(f'Вызвана функция: {function.__name__}   время работы функции: ')
                         file.write(str(time_work))
                except:
                    print(f'Вызвана функция: {function.__name__}   error: FileNotFoundError: {arg} ')
                    print(error_message)
            else:
                try:
                    print(f'Вызвана функция:{function.__name__}')
                    print(f'Время работы фукции: {time_work}')
                except TypeError(error_message):
                    print(f'Вызвана функция:{function.__name__}')
                    print(f'error: ValueError: {error_message}')
            return function
        return inner
    return wrapper


def predical_file_print(file_input: str) -> str:
    return file_input


@decorator_log(predical_file_print, 'Файл для вывода данных не создан')
def example(log_input: str):
    for i in range(1000000):
        continue


if __name__ == '__main__':

    example('../Dat/log.txt')

    example('../Data/log.txt')

    example('')

