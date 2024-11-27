class Product:  # Create an empty class
    """ class for products """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ магический метод, который возвращает объект в читабильном виде """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ функция выводит полную стоимость всех товаров на складе """
        if type(self) is type(other):  # теперь программа складывает все товары одного класса Product
            all_sum = self.quantity * self.price + other.quantity * other.price
            return f'Стоимость всех товаров на складе: {all_sum}'
        raise TypeError

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, dict_of_product: dict):
        products_list = Category.get_product()
        for product in products_list:
            if dict_of_product['name'] in product.name:
                quantity = dict_of_product['quantity'] + product.quantity
                cls.quantity = quantity
            else:
                cls.quantity = dict_of_product['quantity']
        for product in products_list:
            if dict_of_product['name'] == product.name:
                max_price = max(dict_of_product['price'], product.price)
                cls.__price = max_price
        cls.name = dict_of_product['name']
        cls.description = dict_of_product['description']
        cls.quantity = dict_of_product['quantity']
        return Product(cls.name, cls.description, cls.quantity, cls.price)

    @price.setter
    def price(self, price):
        """ сеттер, который проверяет цену на корректность """
        if price < 1:
            raise ValueError('Цена не должна быть нулевая или отрицательная')
        elif price > 0 and self.__price < price:
            print('Цена будет выше предыдущей: Y / N')
            answer = input().lower()
            if answer == 'y':
                self.__price = price

        elif self.__price > price:
            print('Цена будет ниже предыдущей: Y / N')
            answer = input().lower()
            if answer == 'y':
                self.__price = price


class Category:
    """ class for categories """
    name: str
    description: str
    __products = list()

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """ магический метод, который возвращает объект в читабильном виде """
        sum_of_products = 0
        for product in Category.__products:
            sum_of_products += product.quantity
        return f'{self.name}, количество продуктов: {sum_of_products} шт.'

    @staticmethod
    def get_product():
        return Category.__products

# Корректировка метода add_product с использованием проверок добавления продуктов в категории (задание 3)
    @staticmethod
    def add_product(new_product: Product):
        if isinstance(new_product, Product):
            Category.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> list[str]:
        """ геттер, который возвращает список продуктов """
        list_of_products = list()
        for product in Category.__products:
            list_of_products.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n')
        return list_of_products


class TaskIteration:
    """ дополнительный класс для перебора продуктов """
    list_of_products = Category.get_product()

    def __init__(self, list_of_products):
        self.product_list = list_of_products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(Category.get_product()):
            product = self.list_of_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# Для магазина необходимо выделить две категории товаров и создать под них классы

class Smartphone(Product):
    """ смартфон """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ трава газонная """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
