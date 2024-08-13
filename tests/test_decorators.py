import pytest

from src.decorators import decorator_log

from src.decorators import example

def test_decorator_log(capsys):
    decorator_log()
    captured = capsys.readouterr()
    assert captured.out == f"Вызвана функция: example"


def test_decorator_log():
    with pytest.raises(Exception, file_input='../Dat/log.txt'):
        example()

