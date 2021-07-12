class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return f'Vehiculo ->[Color: {self.color}; Ruedas:{self.ruedas}]'


class Bicicleta(Vehiculo):

    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Bicicleta ->[Tipo: {self.tipo}]'

class Coche(Vehiculo):

    def __init__(self, velocidad):
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Coche ->[Velocidad: {self.velocidad}]'
