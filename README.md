## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 99% (отчет: `htmlcov/index.html`)

### Структура тестов

| Файл                     | Что проверяется                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------- |
| `test_bun.py`            | Геттеры `get_name()`, `get_price()` в `Bun`                                         |
| `test_ingredient.py`     | Геттеры `get_name()`, `get_price()`, `get_type()` в `Ingredient`, параметризация    |
| `test_burger.py`         | Логика: `set_buns`, `add/remove/move ingredient`, `get_price()`, чек                |
| `test_database.py`       | Методы `available_buns()`, `available_ingredients()` возвращают валидные объекты    |
| `test_praktikum_main.py` | Тест функции `main()` с моками (`Database`, `Bun`, `Ingredient`) и проверкой вывода |
