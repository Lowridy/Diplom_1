import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_available_methods_return_lists():
    db = Database()
    buns = db.available_buns()
    ings = db.available_ingredients()
    assert isinstance(buns, list)
    assert isinstance(ings, list)
    assert all(isinstance(b, Bun) for b in buns)
    assert all(isinstance(i, Ingredient) for i in ings)

def test_database_content_integrity():
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]
    assert "cutlet" in names
    sauces = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_SAUCE]
    fillings = [i for i in db.available_ingredients() if i.get_type() == INGREDIENT_TYPE_FILLING]
    assert sauces and fillings
