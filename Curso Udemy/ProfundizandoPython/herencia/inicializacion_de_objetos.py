#orden de inicializacion

class Padre:
    def __init__(self):
        print('inicializador padre')

    def metodo(self):
        print('metodo padre')



class Hijo(Padre):
    # si no tiene constructor llama solo al de padre
    def __init__(self):
        print('inic hijo')
        super().__init__()

    def metodo(self):
        print('metodo sobreescrito padre')

padre = Padre()
hijo = Hijo()
hijo.metodo()

