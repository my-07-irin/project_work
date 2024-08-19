from typing import Any, Callable

import pytest

from src.decorators import decorator_log, divining_numbers


def test_decorator_log(path_log=None):

    assert divining_numbers(10, 2) == 5.0
    assert divining_numbers(0, 2) == 0.0
    assert divining_numbers(2, 5) == 0.4

    with pytest.raises(Exception):
        divining_numbers(2, 0)


def test_decorator_log(capsys: Any) -> Any:
    """вывод на консоль"""

    decorator_log(path_log="../Data/")
    captured = capsys.readouterr()
    assert captured.out == ""
