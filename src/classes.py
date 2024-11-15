class Product:  # Create an empty class
    """ class for products """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_of_products):
        name = dict_of_products['name']
        description = dict_of_products['description']
        price = dict_of_products['price']
        quantity = dict_of_products['quantity']
        return cls(name, description, price, quantity)


class Category:
    """ class for categories """
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

    # @property
    # def products(self):
    #     return self.products

    def add_product(self, new_product: Product):
        self.products.append(new_product)
        Category.product_count += 1
        # Category.__products.append(new_product)

    def product_list(self):
        list_of_product = ''
        for product in self.products:
            list_of_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return list_of_product
