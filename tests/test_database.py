import pytest
from unittest.mock import patch, MagicMock
from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_initialization(self):
        """Тест инициализации базы данных"""
        db = Database()
        
        # Проверка, что булочки добавлены
        assert len(db.buns) == 3
        assert isinstance(db.buns[0], Bun)
        assert db.buns[0].get_name() == "black bun"
        assert db.buns[0].get_price() == 100
        
        # Проверка, что ингредиенты добавлены
        assert len(db.ingredients) == 6
        assert isinstance(db.ingredients[0], Ingredient)
        
        # Проверка соусов
        sauces = [i for i in db.ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        
        # Проверка начинок
        fillings = [i for i in db.ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_available_buns(self):
        """Тест метода available_buns"""
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        """Тест метода available_ingredients"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        # Проверка соусов
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        assert sauces[0].get_name() == "hot sauce"
        assert sauces[1].get_name() == "sour cream"
        assert sauces[2].get_name() == "chili sauce"
        
        # Проверка начинок
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        assert fillings[0].get_name() == "cutlet"
        assert fillings[1].get_name() == "dinosaur"
        assert fillings[2].get_name() == "sausage"

    @patch('database.Bun')
    @patch('database.Ingredient')
    def test_database_with_mocks(self, mock_ingredient, mock_bun):
        """Тест базы данных с использованием моков"""
        # Настраиваем моки
        mock_bun.return_value = MagicMock()
        mock_ingredient.return_value = MagicMock()
        
        # Создаем экземпляр базы данных
        db = Database()
        
        # Проверяем, что моки были вызваны нужное количество раз
        assert mock_bun.call_count == 3  # 3 булочки
        assert mock_ingredient.call_count == 6  # 6 ингредиентов 