names1 = ['juan', 'karla', 'pedro']
names2 = 'santiago pablo maria'.split()

#sumar listas
print(names1 + names2)

#extender una lista con otra
names1.extend(names2)  # agrega los elementos de la segunda lista
print(names1)


numeros = [10,20,40,50,30,60,75, 40]

print(numeros)
print(f'indice del numero 40: {numeros.index(40)}')  # de la primera vez q lo encuentra

numeros.reverse()
print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

print(f'valor minimo de la lista {min(numeros)}')
print(f'valor maximo de la lista {max(numeros)}')

# copiar elementos a otra lista
numeros2 = numeros.copy()  # shallow copy copia el contenido pero no la direcion de memoria de la variable contenedora de la lista

print(numeros)
print(numeros2)

numeros2 = list(numeros)
print(numeros)
print(numeros2)

# lista de listas

lista_multiplicacion = 5*[[2, 5]]  # todos los cambios realizados en alguna de estas sublistas impacta en el resto xq cada
                                   # elemento de la principal lista referencia a la misma direccion de memoria
print(lista_multiplicacion)

lista_multiplicacion[0][0]=1
print(lista_multiplicacion)

lista_multiplicacion[0].append(8)
print(lista_multiplicacion)

# matriz
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(matriz)


matriz = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
matriz.sort(key=len)
print(matriz)

matriz = ['juan','karla','pedro','esperanza']
matriz = sorted(matriz)  # ordena los elementos por orden alfabetico ascendente (A=>Z)
print(matriz)
matriz = sorted(matriz, reverse= True)  # ordena los elementos por orden alfabetico descendente (Z=>A)
print(matriz)

matriz = sorted(matriz, key=len)  # ordena por largo del string (ascendente)
print(matriz)

matriz = reversed(matriz)  # ordena por largo del string (ascendente)
print(list(matriz))



