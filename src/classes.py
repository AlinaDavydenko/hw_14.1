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

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, dict_of_products: dict):
        products_list = [Category.products]
        for product in products_list:
            if dict_of_products['name'] == product:
                quantity = dict_of_products['quantity'] + Category.products['quantity']
                cls.quantity = quantity
            else:
                cls.quantity = dict_of_products['quantity']
        for product in products_list:
            max_price = max(dict_of_products['price'], product['price'])
            cls.__price = max_price
        cls.name = dict_of_products['name']
        cls.description = dict_of_products['description']
        # cls.__price = dict_of_products['price']
        cls.quantity = dict_of_products['quantity']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        """ сеттер, который проверяет цену на корректность """
        if price < 1:
            raise ValueError('Цена не должна быть нулевая или отрицательная')
        elif price > 0 and self.__price < price:
            print('Цена выше предыдущей: Y / N')
            answer = input().lower()
            if answer == 'y':
                self.__price = price

        elif self.__price > price:
            print('Цена ниже предыдущей: Y / N')
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

    @property
    def product(self):
        return Category.__products

    @staticmethod
    def add_product(new_product: Product):
        Category.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        """ геттер, который возвращает список продуктов """
        list_of_products = list()
        for product in Category.__products:
            list_of_products.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n')
        return list_of_products
