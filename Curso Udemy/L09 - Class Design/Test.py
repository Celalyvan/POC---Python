from Order import Order
from Product import Product

product3 = Product('medias', 50)
product4 = Product('blusa', 750)


order = Order([Product('oreo', 80.00), Product('queso', 150.00)])

print(order.__str__())

print(f'Final price: ${order.get_Total()}')

order.add_product(product3)
order.add_product(product4)

print(order.__str__())

print(f'Final price: ${order.get_Total()}')