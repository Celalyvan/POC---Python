# Solicitar al usuario dos valores:
#
#   numero1 (int)
#
#    numero2 (int)
#
# Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
#
#   Proporciona el numero1:
#    Proporciona el numero2:
#   El numero mayor es:<numeroMayor>

numero1 = int(input("proporcionar el numero 1: "))
numero2 = int(input("proporcionar el numero 2: "))

if numero1 > numero2:
    print("el mayor numero es", numero1)
else:
    print("el mayor numero es", numero2)


print(f'''
esta forma de escribir impreisones
    respeta los saltos de renglones y tabulaciones
a la vez que facilita la impresion de variables: {numero1}
''')
