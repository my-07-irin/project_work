import pytest
from pathlib import Path
from time import time
from typing import Any, Callable
from src.decorators import decorator_log
from src.decorators import example

def test_decorator_log(capsys):
    decorator_log(function=example)
    captured = capsys.readouterr()
    assert captured.out == ''


# def test_example(path_input: str) -> Any:
#     if Path(path_input).exists is False:
#         raise ValueError('директория для выходного файла не найдена')
#     return path_input

