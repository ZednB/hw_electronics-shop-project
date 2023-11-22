import pytest
from src.phone import Phone


def test_phone():
    phone = Phone("Iphone11", 35000, 30, 1)
    assert phone.name == "Iphone11"
    assert phone.price == 35000
    assert phone.quantity == 30
    assert phone.number_of_sim == 1


def test_repr_phone():
    phone1 = Phone("Samsung", 30000, 20, 2)
    assert repr(phone1) == "Phone('Samsung', 30000, 20, 2)"

