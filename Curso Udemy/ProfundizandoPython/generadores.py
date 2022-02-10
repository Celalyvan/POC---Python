# funcion para retornar secuencia de valores regresados en secuencia
# no se usa return sino yield

def generador():
# cada vez q llega a un yield se suspende la ejecucion de la funcion
# esta retoma cuando se vuelve a ingresar al metodo
    yield 1
    yield 2
    yield 3


gen = generador()  # debo asignarlo a una variable
# si consumo mas valores de los retornados, lanza excepcion
print(next(gen))
print(next(gen))
print(next(gen))

for valor in generador():  # al volver a llamar al metodo se refrescan los valores
    print(f'numero generado {valor}')

