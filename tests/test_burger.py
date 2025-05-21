import pytest
from unittest.mock import MagicMock, patch
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.burger = Burger()
        
        # Создаем мок для булочки
        self.mock_bun = MagicMock(spec=Bun)
        self.mock_bun.get_name.return_value = "test bun"
        self.mock_bun.get_price.return_value = 100
        
        # Создаем моки для ингредиентов
        self.mock_sauce = MagicMock(spec=Ingredient)
        self.mock_sauce.get_name.return_value = "test sauce"
        self.mock_sauce.get_price.return_value = 50
        self.mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        
        self.mock_filling = MagicMock(spec=Ingredient)
        self.mock_filling.get_name.return_value = "test filling"
        self.mock_filling.get_price.return_value = 150
        self.mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    def test_initialization(self):
        """Тест инициализации бургера"""
        assert self.burger.bun is None
        assert len(self.burger.ingredients) == 0

    def test_set_buns(self):
        """Тест установки булочек"""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        self.burger.add_ingredient(self.mock_sauce)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_sauce
        
        self.burger.add_ingredient(self.mock_filling)
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[1] == self.mock_filling

    def test_remove_ingredient(self):
        """Тест удаления ингредиента"""
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        assert len(self.burger.ingredients) == 2
        
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_filling

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        
        # Перемещаем соус с позиции 0 на позицию 1
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == self.mock_filling
        assert self.burger.ingredients[1] == self.mock_sauce

    def test_get_price(self):
        """Тест расчета цены бургера"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        
        # Цена = (цена булочки * 2) + цена соуса + цена начинки
        expected_price = (100 * 2) + 50 + 150
        assert self.burger.get_price() == expected_price
        
        # Проверяем, что методы моков были вызваны
        self.mock_bun.get_price.assert_called()
        self.mock_sauce.get_price.assert_called()
        self.mock_filling.get_price.assert_called()

    def test_get_receipt(self):
        """Тест получения чека"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        
        receipt = self.burger.get_receipt()
        
        # Проверяем содержимое чека
        assert "(==== test bun ====)" in receipt
        assert "= sauce test sauce =" in receipt
        assert "= filling test filling =" in receipt
        assert "Price: 400" in receipt  # (100 * 2) + 50 + 150 = 400
        
        # Проверяем, что методы моков были вызваны
        self.mock_bun.get_name.assert_called()
        self.mock_bun.get_price.assert_called()
        self.mock_sauce.get_type.assert_called()
        self.mock_sauce.get_name.assert_called()
        self.mock_filling.get_type.assert_called()
        self.mock_filling.get_name.assert_called()

    @patch('burger.Burger.get_price')
    def test_get_receipt_with_patched_price(self, mock_get_price):
        """Тест получения чека с патченной ценой"""
        mock_get_price.return_value = 999
        
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_sauce)
        
        receipt = self.burger.get_receipt()
        
        # Проверяем, что в чеке используется патченная цена
        assert "Price: 999" in receipt
        mock_get_price.assert_called_once() 