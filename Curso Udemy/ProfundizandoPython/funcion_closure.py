# funcion q define a otra y la regresa
# la funcion anidadda puede acceder a las funciones superiores o externas

def operacion(a, b):
    def sumar():
        return a+b

    return sumar


mi_closure = operacion(5, 2)
print(f' resultado closure: {mi_closure()}')
print(f' resultado closure: {operacion(5, 2)()}')




