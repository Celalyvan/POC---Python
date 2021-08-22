from Square import Square

print('Creatin Square'.center(50, '-'))
square1 = Square(9, 'rojo')
print(square1.width)
print(square1.height)
print(square1.color)

print(square1.calculate_area())

# MRO - Method Resolution Order
print(Square.mro())
