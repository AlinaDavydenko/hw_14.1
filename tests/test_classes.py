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


# тестирование магических методов
# тестирование str
def test_str_method(product_init):
    product1 = product_init
    assert str(product1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


@pytest.fixture
def product_1():
    product1 = Product("Samsung", "Серый цвет", 180000.0, 5)
    return product1


@pytest.fixture
def product_2():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product2


# тестирование add
def test_add_products(product_1, product_2):
    assert product_1 + product_2 == 'Стоимость всех товаров на складе: 2580000.0'


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


@pytest.fixture
def all_products():
    product1 = Product(
        "Samsung", "Серый цвет", 18, 5)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство",
        [product1])
    return category1


def test_add_product(all_products):
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    all_products.add_product(product4)
    assert Category.product_count == 2


# тестирование магических методов
def test_str_for_categories(all_products):
    products = all_products
    assert str(products) == 'Смартфоны, количество продуктов: 5 шт.'
