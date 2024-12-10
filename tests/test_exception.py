import pytest

from src.classes import Product, Category, LawnGrass, Smartphone


@pytest.fixture
def category_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", [],
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", [], 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", [], 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    return category1


def test_middle_price(category_product):
    category = category_product
    with pytest.raises(TypeError):
        category.middle_price()


def test_product():
    with pytest.raises(ValueError):
        Product('a', 's', 0, 0)


def test_product_add():
    grass = LawnGrass('q', 'w', 1, 2, 'e', 'r', 't')
    phone = Smartphone('q', 'w', 1, 2, 'e', 'r', 't', 'i')
    with pytest.raises(TypeError):
        Product.__add__(grass, phone)

