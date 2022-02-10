# generador anonimo

# las expresiones generadoras en estos casos deben ir entre ()
# primero debe anotarse el retorno
multiplicacion = (valor*valor for valor in range(4))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))


# pasando expresion generadora a una funcion
# en estos casos no lleva ()

import math
suma = sum(valor*valor for valor in range(4))
print(f'resultado suma {suma}')

lista = ['juan', 'perez']
generador = (valor for valor in lista)
print(next (generador))
print(next (generador))


lista = ['karla', 'gomez']
contador = 0


def incrementar():
    global contador
    contador += 1
    return contador


generador = (f'{incrementar()} . {nombre}' for nombre in lista)
lista = list(generador)
print(lista)