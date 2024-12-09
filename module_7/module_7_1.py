from pprint import pprint


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        res = file.read()
        file.close()
        return res

    def add(self, *products: Product):
        request = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.__str__() in request:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product.__str__()}\n')
        file.close()


def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


if __name__ == '__main__':
    main()