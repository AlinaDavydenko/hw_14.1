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

    @classmethod
    def new_product(cls, dict_of_products):
        name = dict_of_products['name']
        description = dict_of_products['description']
        price = dict_of_products['price']
        quantity = dict_of_products['quantity']
        return cls(name, description, price, quantity)

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
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1
        # Category.__products.append(new_product)

    @property
    def product_list(self):
        """ геттер, который возвращает список продуктов """
        list_of_product = ''
        for product in self.__products:
            list_of_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return list_of_product
