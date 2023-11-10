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
