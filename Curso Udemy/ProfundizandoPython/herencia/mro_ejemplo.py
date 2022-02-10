class Clase1:
    def __init__(self):
        print('init calse1')

    def metodo(self):
        print('metodo clase1')

class Clase2(Clase1):
    def __init__(self):
        print('init calse2')

    def metodo(self):
        print('metodo clase2')


class Clase3(Clase1):
    def __init__(self):
        print('init calse3')

    def metodo(self):
        print('metodo clase3')

class Clase4(Clase2, Clase3):
    # def __init__(self):
    #     print('init calse4')

    def metodo(self):
        print('metodo clase4')


clase4 = Clase4()
print(Clase4.__bases__)
print(Clase4.__mro__)
