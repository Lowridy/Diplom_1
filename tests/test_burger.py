import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.mark.parametrize("bun_price, ing_prices, expected_total", [
    (5.0, [1.0], 5.0*2 + 1.0),
    (10.0, [2.5, 3.5], 10.0*2 + 2.5 + 3.5),
])
def test_get_price_with_mocked_components(bun_price, ing_prices, expected_total):
    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price

    mock_ingredients = []
    for p in ing_prices:
        m = Mock()
        m.get_price.return_value = p
        mock_ingredients.append(m)

    burger = Burger()
    burger.set_buns(mock_bun)

    for m in mock_ingredients:
        burger.add_ingredient(m)

    total = burger.get_price()

    mock_bun.get_price.assert_called()
    for m in mock_ingredients:
        m.get_price.assert_called_once()

    assert total == expected_total
