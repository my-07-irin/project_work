import pytest
import os
from pathlib import Path
from time import time
from typing import Any, Callable
from src.decorators import decorator_log
from src.decorators import example

def test_decorator_log(capsys):
    decorator_log(function=example)
    captured = capsys.readouterr()
    assert captured.out == ''


def test_example() -> Any:
    path_input = example('')
    assert path_input == ''

def test_example() -> Any:
    path_input = example('../Data/')
    assert path_input == ',,/Data/'


def test_decorator_log():
    @decorator_log
    def example(path_input: str) -> Any:
        for i in range(1000000):
            continue
        return path_input
    path_log = example('../data/')
    assert path_log == ',,/data/'


def test_decorator_log():
    @decorator_log
    def example(path_input: str) -> Any:
        for i in range(1000000):
            continue
        return path_input
    path_log = example('../dat/')
    assert path_log == ',,/dat/'


