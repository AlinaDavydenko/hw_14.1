import pytest

from src.classes import Product, Category


@pytest.fixture
def category_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    return category1


def test_middle_price(category_product):
    category = category_product
    with pytest.raises(ZeroDivisionError):
        category.middle_price()
