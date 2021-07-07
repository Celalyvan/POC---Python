def miFuncionEnPython(nomre, apellido):
    print('saludos desde la funcion:', nomre, apellido)


miFuncionEnPython('Juan', 'Suarez')


#  no puedo invocar una funcion sin haberla definido previamente

# def sumar(a:int =0, b:int=0) -> int:  son sugerencias del tipo de dato que deberia tener los parametros
def sumar(a=0, b=0):  # nota, no se declara tipo de dato de retorno de la funion
    return a + b


resultado = sumar(3, 5)

print(resultado)

print(sumar())

def listarNombres(*nombres):  # de esta forma se que voy a recibir varios pero no se cuantos parametros y lo convierte a tupla
    for nombre in nombres:
        print(nombre)


listarNombres('juan', 'Karla', 'Jacinto')
listarNombres('Tito', 'Tito')
