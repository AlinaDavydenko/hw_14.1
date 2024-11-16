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
        for element in Category.product:
            if dict_of_products['name'] == element['name']:
                quantity = dict_of_products['quantity'] + Category.product['quantity']
                cls.quantity = quantity
            else:
                cls.quantity = dict_of_products['quantity']
        name = dict_of_products['name']
        description = dict_of_products['description']
        price = dict_of_products['price']
        # quantity = dict_of_products['quantity']
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


# проверка
if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    # print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)