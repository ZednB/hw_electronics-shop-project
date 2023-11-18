"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    item1 = Item('Смартфон', 10000, 20)
    item2 = Item('Ноутбук', 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item = Item('Смартфон', 20.0, 5)
    item.pay_rate = 1
    item.apply_discount()
    assert item.price == 20.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_get_name():
    item = Item("TestItem", 4, 5)
    assert item.name == "TestItem"


def test_set_name():
    item = Item("TestItem", 4, 5)
    item.name = "Test"
    assert item.name == "Test"
    item.name = "TestItem_set"
    assert item.name == "TestItem_s"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 5


def test_repr():
    item = Item("Телефон", 25000, 40)
    assert repr(item) == 'Item(Телефон, 25000, 40)'


def test_str():
    item = Item("Телефон", 25000, 40)
    assert str(item.name) == "Телефон"
    item = Item("Смартфон", 25000, 40)
    assert str(item.name) == "Смартфон"
