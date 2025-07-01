import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger

@pytest.fixture
def basic_bun():
    return Bun("bun", 5.0)

@pytest.fixture
def burger_with_bun(basic_bun):
    b = Burger()
    b.set_buns(basic_bun)
    return b
