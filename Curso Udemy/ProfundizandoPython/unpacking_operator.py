numbers = [1,2,3]

print(numbers)
print(*numbers)
print(*numbers, sep=' - ')



def sumar(a, b, c):
    return a+b+c


print(sumar(*numbers))

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(lista3)
lista3 = [*lista1, *lista2]
print(lista3)


# para diccionarios se usa **

dicc1 = {'A':1,'B':2,'C':3}
dicc2 = {'D':4,'E':5,'F':6}
dicc3 = {**dicc1,**dicc2}
print(dicc3)

lista = [*'helloworld']
print(lista)



