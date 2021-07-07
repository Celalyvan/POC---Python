# key - value Collection

diccionario = {
    'IDE': 'integrated development Eviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Managment System'
}

print(diccionario)

# largo
print(len(diccionario))

#
print(diccionario['IDE'])

print(diccionario.get('IDE'))

# modificar
diccionario['IDE'] = 'Todo en mayus'
print(diccionario['IDE'])

#recorre todos los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

print('\n keys')
for termino in diccionario.keys():
    print(termino, valor)

print('\n values')
for termino in diccionario.values():
    print(termino, valor)

# comprobar existencias de algun elemento
print('IDE' in diccionario)

#agregar elem
diccionario['PK'] = 'Primary Key'

print(diccionario)

#remover
diccionario.pop('DBMS')

print(diccionario)

# limpiar diccionario
diccionario.clear()
print(diccionario)

# eliminar por completo
del diccionario
print(diccionario)
