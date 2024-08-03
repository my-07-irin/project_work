import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("0987654321098765", "0987 65** **** 8765"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("73654108430135874305", "7365 41** **** 3587"),
        ("736", "номер карты введён неверно"),
        ("73 65 41 08 43 01 35", "номер карты введён неверно"),
        ("", ""),
    ],
)
def test_get_mask_card_number(number: str, expected: str) -> str:
    """тестирование функции get_mask_card_number из masks.py"""
    assert get_mask_card_number(number) == expected
    return expected


@pytest.mark.parametrize(
    "account,expected",
    [
        ("0987654321098765", "**8765"),
        ("7000792289606361", "**6361"),
        ("73654108430135874305", "**4305"),
        ("73654108430135", "**0135"),
        ("736", "номер счёта введён неверно"),
        ("73 65 41 08 43 01 35", "номер счёта введён неверно"),
        ("", ""),
    ],
)
def test_get_mask_account(account: str, expected: str) -> str:
    """тестирование функции get_mask_account из masks.py"""
    assert get_mask_account(account) == expected
    return expected
