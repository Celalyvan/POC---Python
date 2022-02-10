# funciones anonimas y pequeñas (1 linea de codigo)
# y no necesita () para los parametros y no es necesario
# la palabra return pero si debe retornar una expresion valida


#funcion normal
def sumar(a,b):
    return a+b


funcion_lambda = lambda a, b: a+b

resultado = funcion_lambda(4,58)
print(resultado)

funcion_lambda = lambda: 'aloja'
print(f'llamada a lambda: {funcion_lambda()}')

#parametros x default
funcion_lambda = lambda a=2, b=5: a+b

print(f'llamado a lambda con valores default: {funcion_lambda()}')
print(f'llamado a lambda con valores default pero pasando parametros: {funcion_lambda(7,8)}')

# lambda con *args y **kwargs
funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'resultado de argumentos variables: {funcion_lambda(1,2,3, a=5,b=6)}')



