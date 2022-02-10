class ListaSimple:

    def __init__(self, elementos):
        self._elementos = list(elementos)


    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, index):
        return self._elementos[index]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r}'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # ordenamos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()


class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


# la clase de la izquierda toma mas prioridad
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

lista_ordenada = ListaOrdenada([4,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(7)
print(lista_ordenada)


lista_EO = ListaEnterosOrdenada([4,5,-1,10,14,-4])
print(lista_EO)
lista_EO.agregar(8)
print(lista_EO)

# MRO (method resolution order)
print(ListaEnterosOrdenada.__mro__)