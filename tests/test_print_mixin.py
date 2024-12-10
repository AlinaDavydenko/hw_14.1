from src.classes import Product, Category


def test_mixin_product(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 180000.0, 5)'


def test_mixin_category(capsys):
    Category("Телевизоры", "Современный телевизор", [])
    message = capsys.readouterr()
    print(message)
    assert message.out.strip() == ''
