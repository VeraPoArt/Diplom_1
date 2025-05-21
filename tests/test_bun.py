import pytest
from bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ],
    )
    def test_bun_initialization(self, name, price):
        """Тест инициализации булочки с разными параметрами"""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ],
    )
    def test_get_name(self, name, price):
        """Тест метода get_name"""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ],
    )
    def test_get_price(self, name, price):
        """Тест метода get_price"""
        bun = Bun(name, price)
        assert bun.get_price() == price 