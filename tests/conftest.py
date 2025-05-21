import pytest
from unittest.mock import MagicMock
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    mock = MagicMock(spec=Bun)
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_sauce():
    """Фикстура для создания мока соуса"""
    mock = MagicMock(spec=Ingredient)
    mock.get_name.return_value = "test sauce"
    mock.get_price.return_value = 50
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def mock_filling():
    """Фикстура для создания мока начинки"""
    mock = MagicMock(spec=Ingredient)
    mock.get_name.return_value = "test filling"
    mock.get_price.return_value = 150
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock 