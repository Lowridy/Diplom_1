from unittest.mock import Mock, patch
import praktikum.praktikum as pk

def test_main_flow_with_print_patched():
    fake_db = Mock()
    fake_bun = Mock(get_name=lambda: "MockBun", get_price=lambda: 5.0)

    def mk_ing(name, price):
        m = Mock()
        m.get_type.return_value = "SAUCE"
        m.get_name.return_value = name
        m.get_price.return_value = price
        return m

    ingredients = [mk_ing(f"I{i}", i) for i in range(6)]
    fake_db.available_buns.return_value = [fake_bun]
    fake_db.available_ingredients.return_value = ingredients

    with patch('praktikum.praktikum.Database', return_value=fake_db), \
         patch('praktikum.praktikum.print') as mock_print:
        pk.main()

    assert mock_print.called, "print в main() должен был быть вызван"

    printed = " ".join(arg[0] for call in mock_print.call_args_list for arg in call[0:1]).lower()

    assert "mockbun" in printed
    assert "i1" in printed and "i3" in printed and "i4" in printed
    assert "i5" not in printed
    assert "price:" in printed
    assert "18" in printed
