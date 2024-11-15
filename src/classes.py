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

    @price.setter
    def price(self, price):
        if price < 1:
            raise ValueError('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = price

    @property
    def get_price(self):
        return self.__price


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

    # @property
    # def products(self):
    #     return self.products

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


# new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})

# print(Category.products)   # Такого нет

# print(new_product.name)
# print(new_product.description)
# print(new_product.price)
# print(new_product.quantity)
