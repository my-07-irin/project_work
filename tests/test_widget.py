import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("736", "не выбран тип карты"),
        ("73 65 41 08 43 01 35", "не выбран тип карты"),
        ("", ""),
    ],
)
def test_mask_account_card(number: str, expected: str) -> str:
    """тестирование функции mask_account_card из widget.py"""
    assert mask_account_card(number) == expected
    return expected


@pytest.mark.parametrize(
    "account,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("03-11", "дата введена неверно"),
        ("", ""),
    ],
)
def test_get_date(account: str, expected: str) -> str:
    """тестирование функции get_date из widget.py"""
    assert get_date(account) == expected
    return expected
