# (Eng: tuple) respeta el orden de adicion pero no se pueden modificar
# si se agrega un solo elemento se notaria asi: frutas = ('naranja', )
frutas = ('naranja', 'banana', 'guayaba')

print(len(frutas))

print(frutas)

# acceder a un elem

print(frutas[0])
print(frutas[-1])

# rango de valores
print(frutas[1:2])  # sin incluir el ultimo indice

for fruta in frutas:
    print(fruta, end=' ')  # el valor end me permite agregar algo al final de la impresion de cada linea

# cambiar valor de tupla seria necesario convertir la tupla a lista y nuevamente a tupla
frutasLista = list(frutas)
frutasLista[0]= 'pera'
frutas= tuple(frutasLista)

print('\n', frutas)


