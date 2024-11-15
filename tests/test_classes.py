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


@pytest.fixture
def product_method():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    return new_product


def test_new_product(product_method):
    assert product_method.name == "Samsung Galaxy S23 Ultra"
    assert product_method.description == "256GB, Серый цвет, 200MP камера"


# testing of class Category
@pytest.fixture
def category_init():
    return Category("Телевизоры", "Современный телевизор", [])


def test_init_2(category_init):
    assert category_init.name == "Телевизоры"
    assert category_init.description == "Современный телевизор"
    assert category_init.products == []

    assert category_init.category_count == 1
    assert category_init.product_count == 0
