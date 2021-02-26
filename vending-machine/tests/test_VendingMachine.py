import pytest
from model.VendingMachine import VendingMachine
from model.MoneyStack import MoneyStack
from model.Item import Item


def test_vending_machine_creation():
    vending_machine = VendingMachine()
    assert vending_machine.machine_stack.get_total_value() == 7000
    assert vending_machine.vending_stack.get_total_value() == 0


def test_insert_nickel():
    vending_machine = VendingMachine()
    vending_machine.insert_nickel()
    assert vending_machine.vending_stack.nickels == 1


def test_insert_dime():
    vending_machine = VendingMachine()
    vending_machine.insert_dime()
    assert vending_machine.vending_stack.dimes == 1


def test_insert_quarter():
    vending_machine = VendingMachine()
    vending_machine.insert_quarter()
    assert vending_machine.vending_stack.quarters == 1


def test_insert_dollar():
    vending_machine = VendingMachine()
    vending_machine.insert_nickel()
    assert vending_machine.vending_stack.nickels == 1


def test_coin_return():
    vending_machine = VendingMachine()
    vending_machine.insert_nickel()
    vending_machine.insert_dime()
    vending_machine.insert_quarter()
    vending_machine.insert_dollar()
    returned_coins: MoneyStack = vending_machine.coin_return()
    assert returned_coins.dollars == 1
    assert returned_coins.quarters == 1
    assert returned_coins.dimes == 1
    assert returned_coins.nickels == 1


def test_service():
    vending_machine = VendingMachine()
    vending_machine.service()  # Note : this is called as part of the constructor, but calling it again will do no harm
    assert len(vending_machine.item_slots['A']) == 2
    assert len(vending_machine.item_slots['B']) == 2
    assert len(vending_machine.item_slots['C']) == 2
    assert vending_machine.machine_stack.nickels == 50
    assert vending_machine.machine_stack.dimes == 50
    assert vending_machine.machine_stack.quarters == 50
    assert vending_machine.machine_stack.dollars == 50


def test_vend_item():
    vending_machine = VendingMachine()
    vending_machine.insert_dollar()
    your_stuff: (Item, MoneyStack) = vending_machine.vend_item('B')
    assert your_stuff[0].name == "Mars Bars"
    assert your_stuff[0].price == 100
    assert your_stuff[1].dollars == 0
    assert your_stuff[1].quarters == 0
    assert your_stuff[1].dimes == 0
    assert your_stuff[1].nickels == 0


def test_vend_item_not_enough_money():
    vending_machine = VendingMachine()
    your_stuff: (Item, MoneyStack) = vending_machine.vend_item('B')
    assert your_stuff is None


def test_return_change_none_required():
    vending_machine = VendingMachine()
    vending_machine.insert_dollar()
    vending_machine.insert_quarter()
    vending_machine.insert_quarter()
    your_stuff: (Item, MoneyStack) = vending_machine.vend_item('C')
    assert your_stuff[1].nickels == 0
    assert your_stuff[1].dimes == 0
    assert your_stuff[1].quarters == 0
    assert your_stuff[1].dollars == 0


def test_return_change_correct_amount():
    vending_machine = VendingMachine()
    vending_machine.insert_dollar()
    vending_machine.insert_dollar()
    your_stuff: (Item, MoneyStack) = vending_machine.vend_item('C')
    assert your_stuff[1].nickels == 0
    assert your_stuff[1].dimes == 0
    assert your_stuff[1].quarters == 2
    assert your_stuff[1].dollars == 0


def test_return_change_not_enough_coins():
    vending_machine = VendingMachine()
    vending_machine.machine_stack.nickels = 0
    vending_machine.machine_stack.dimes = 0
    vending_machine.machine_stack.quarters = 0
    vending_machine.machine_stack.dollars = 0
    vending_machine.insert_dollar()
    your_stuff: (Item, MoneyStack) = vending_machine.vend_item('A')
    assert your_stuff[1].nickels == 0
    assert your_stuff[1].dimes == 0
    assert your_stuff[1].quarters == 0
    assert your_stuff[1].dollars == 0
