import json

from src.classes import Product, Category


def read_json(path: str) -> dict:
    """ for read json file """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def create_objects_from_read_json(data):
    """ the function reads data from the function read_json and creates objects """
    categories = []
    products = []
    [products.append(Product(**product)) for category in data for product in category['products']]
    [categories.append(Category(**category)) for category in data]
    return categories, products


# if __name__ == '__main__':
#     print(read_json('../data/products.json'))
#
#
# if __name__ == '__main__':
#     inf = read_json('../data/products.json')
#     print(create_objects_from_read_json(inf))
