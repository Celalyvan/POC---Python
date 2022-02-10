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


lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

lista_ordenada = ListaOrdenada([4,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(7)
print(lista_ordenada)
