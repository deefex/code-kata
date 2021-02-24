import pytest
from model.MoneyStack import MoneyStack


def test_money_stack_creation():
    money_stack: MoneyStack = MoneyStack()
    assert money_stack.get_total_value() == 0


def test_add_to_money_stack():
    money_stack: MoneyStack = MoneyStack()
    money_stack.add_to_stack(1, 1, 1, 1)
    assert money_stack.get_total_value() == 140
