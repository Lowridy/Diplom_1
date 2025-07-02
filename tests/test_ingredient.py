import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("itype,name,price", [
    (INGREDIENT_TYPE_SAUCE, "sauce1", 1.0),
    (INGREDIENT_TYPE_FILLING, "meat", 10.5),
])
def test_ingredient_basic(itype, name, price):
    ing = Ingredient(itype, name, price)
    assert ing.get_type() == itype
    assert ing.get_name() == name
    assert ing.get_price() == price
