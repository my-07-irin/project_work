from typing import Any, Callable

import sys

import pytest

from src.decorators import decorator_log, divining_numbers


@decorator_log()
def test_decorator_log():

    assert divining_numbers(10, 2) == 5.0
    assert divining_numbers(0, 2) == 0.0
    assert divining_numbers(2, 5) == 0.4

    with pytest.raises(Exception):
        divining_numbers(2, 0)


@decorator_log()
def test_decorator_to_terminal(capsys: Any) -> Any:

    result = divining_numbers(2, 5)
    captured = capsys.readouterr()
    assert captured.out == result

    result = divining_numbers(2, 0)
    captured = capsys.readouterr()
    assert captured.err == result
