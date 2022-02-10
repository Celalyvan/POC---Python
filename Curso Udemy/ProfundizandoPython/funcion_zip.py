# el zip puede mezclar iterables de diferente tipo
numbers = (1,2,3)
letters = ['a','b','c','d']
ids = 232,234,235,236,237
mix = zip(numbers, letters, ids)  # el tamaño del iterable resultado es igual al iterable de menor cantidad, en este caso 3
print(list(mix))

# iterar en paralelo usando zip
for number, letter, id in zip(numbers, letters, ids):
    print(f'numero {number}, letra {letter}, id {id}')


nueva_lista = []
for number, letter, id in zip(numbers, letters, ids):
    nueva_lista.append(f'{number}-{letter}-{id}')

print(nueva_lista)


# emular un unzip
nl = [(1,'a'), (2,'b'), (3,'c')]
numero, letra = zip(*nl)
print(f'n {numero} l {letra} id {id}')

# creando diccionario con zip y 2 iterables
keys = ['nombre', 'apellido','edad']
values = ['juan','perez',18]
diccionario = dict(zip(keys, values))
print(diccionario)


# update al diccionario
llave = ['edad']
new_age = [22]

diccionario.update(zip(llave,new_age))
print(diccionario)


