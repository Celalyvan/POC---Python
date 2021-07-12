from Persona import Persona  # puedo hacer import * para traer todas las clases

print('creacion de objetos'.center(40, '-'))
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()

print('eliminacion de objetos'.center(40, '-'))
del persona2

