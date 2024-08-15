import os
from typing import Any, Callable

import pytest

from src.decorators import decorator_log, example


def test_decorator_log(capsys: Any) -> Callable:
    """тестирование вывода на консоль"""
    decorator_log(function=example)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_example() -> Any:
    path_input = example("")
    assert path_input == ""

    path_input = example("../Data/")
    assert path_input == ",,/Data/"


def test_decorator_log() -> Callable:
    @decorator_log
    def example(path_input: str) -> Any:
        for i in range(1000000):
            continue
        return path_input

    path_log = example("../data/")
    assert path_log == ",,/data/"

    path_log = example("../dat/")
    assert path_log == ",,/dat/"

