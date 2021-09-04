from Product import Product

class Order:
    order_Counter = 0

    def __init__(self, products):
        Order.order_Counter += 1
        self._order_id = Order.order_Counter
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)

    def get_Total(self):
        total = 0
        for product in self._products:
            total += product.product_price

        return total

    def __str__(self):
        products_str = ''

        for product in self._products:
            products_str += product.__str__() + '|\n '

        return f'Orden_ {self._order_id}:\n Products_ {products_str}'





