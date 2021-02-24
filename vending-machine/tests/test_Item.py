import pytest
from model.Item import Item


def test_item_creation():
    item = Item("Mars Bar", 65)
    assert item.name == "Mars Bar"
    assert item.price == 65
