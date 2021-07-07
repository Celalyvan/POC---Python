names = ["Juan", "Karla", "Ricardo", "Maria"]

for i in names:
    print(f'Value : {i}')

print(names)

for i in range(4): # hace la cantidad de iteraciones como numeros pusimos en range()
    print(names[i])
# si pongo numero negativo como index los toma comenzando desde el final
print(f'con indice -2: {names[-2]}')

print(f'con rango de indices: {names[0:2]}')  # hace hasta el 2 no inclusive

print(f'con rango de indices: {names[1:]}')  # recorre desde el indice indicado hasta el final

#  consultar largo de lista
print(len(names))  # len() retorna la cantidad (length) de una lista

#  pisar el valor en ese index
names[3] = 'Ivone'

# add elements
names.append('Lorenzo')

print(names)

#  insertar en un index especifico
names.insert(1, 'Octavio')  # Inserta en el indice 1 desplazando al resto 1 a la derecha

print(names)

# remover 1 elemento
names.remove('Octavio')  # se remueve por valor

print(names)

#  remover el ultimo agregado
names.pop()
print(names)

#  remover del index especificado
del names[0]

print(names)

# eliminar todos los elementos (vaciar la lista)
names.clear()

print(names)

# borrar la lista de memoria
del names

print(names)  # tira error xq no existe mas la lista
