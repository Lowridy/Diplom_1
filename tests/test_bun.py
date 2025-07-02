import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name,price", [
    ("classic", 10.0),
    ("zero", 0.0),
    ("premium", 99.99),
])
def test_bun_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
