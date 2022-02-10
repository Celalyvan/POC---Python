# las funciones son first class citizens
# lo cual significa que se pueden manipular como un objeto


def sumar(a,b):
    return a+b

def operaicon(a,b, funcion):
    print(f'resultado: {funcion(a,b)}')

operaicon(1, 4, sumar)  # puedo pasar una funcion por parametro


# retornar una funcion - se pueden guardar funciones en variables!


def return_funcion():
    return sumar


returned_funcion = return_funcion()
print(f'funcion retornada {returned_funcion(1,2)}')




