class Product:
    product_counter = 0

    def __init__(self, name, price):
        Product.product_counter += 1
        self._product_id = Product.product_counter
        self._product_name = name
        self._product_price = price

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, newId):
        self._product_id = newId

    @property
    def product_name(self):
        return self.product_name

    @product_name.setter
    def product_name(self, newName):
        self._product_name = newName

    @property
    def product_price(self):
        return self._product_price

    @product_price.setter
    def product_price(self, newPrice):
        self._product_price = newPrice

    def __str__(self):
        return f'Product : Id_ {self._product_id}; Name_ {self._product_name}; Price_ ${self._product_price}'


if __name__ == '__main__':
    product1 = Product('oreo', 80.00)
    print(product1)
    product2 = Product('queso', 150.00)
    print(product2)

