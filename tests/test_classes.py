import pytest

from src.classes import Category, Product


# testing of class Product
@pytest.fixture
def product_init():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)


def test_init_1(product_init):
    assert product_init.name == "Samsung Galaxy S23 Ultra"
    assert product_init.description == "256GB, Серый цвет"
    assert product_init.price == 180000.0
    assert product_init.quantity == 5


# testing of class Category
@pytest.fixture
def category_init():
    return Category("Телевизоры", "Современный телевизор", [])


def test_init_2(category_init):
    assert category_init.name == "Телевизоры"
    assert category_init.description == "Современный телевизор"
    assert category_init.products == []

# вопросы с тестами, птест не находит ???
