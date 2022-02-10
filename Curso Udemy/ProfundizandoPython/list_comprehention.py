# usa lista en lugar de tuplas
numeros = range(10)
lista_par = []

for numero in numeros:
    if numero % 2 ==0:
        lista_par.append(numero*numero)

print(lista_par)


# lo mismo pero con list comprehentions
# [expresion for var in collection if condition]
lista_par = []
lista_par = [numero*numero for numero in numeros if numero % 2 ==0]
print(lista_par)

pares = [numero for numero in range(50) if numero % 2 == 0 and numero % 6 == 0]
print(pares)

lista_par = []
lista_impar = []
[lista_par.append(numero) if numero % 2 == 0 else lista_impar.append(numero) for numero in range(50)]
print(f'lista par {lista_par}')
print(f'lista impar {lista_impar}')

# lista de listas
matrix = [[1,2,3],[4,5,6],[7,8,9,10]]

# matriz =>lista
lista = [valor
         for sublista in matrix
         for valor in sublista]
print(f'lista de matriz {lista}')

