import pytest

from src.decorators import decorator_log

from src.decorators import example

def test_decorator_log(capsys):
    decorator_log()
    captured = capsys.readouterr()
    assert captured.out == f"Вызвана функция: example"


def test_decorator_log(predical_file_print):
    with pytest.raises(ValueError, predical_file_print):
        example('../Dat/log.txt')


def test_example(file_input):
    with pytest.raises(OSError, file_input, error_message='Файл для вывода данных'):
        example('../Dat/log.txt')

