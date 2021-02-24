import pytest
from model.Money import Money


def test_money_creation():
    money: Money = Money()
    assert money.NICKEL == 5
    assert money.DIME == 10
    assert money.QUARTER == 25
    assert money.DOLLAR == 100
