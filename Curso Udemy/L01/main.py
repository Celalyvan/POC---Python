x: str = "holus" #:str  es un hint, no determina el tipo de dato a asignar, es una referencia
print(x)

print(type(x))

x = True #valores booleanos van con mayusculas
print(x)

print(type(x))

#Manejo de Strings

miGrupoFavorito = "Slipknot" + "BiS"

print("my favourite band is " + miGrupoFavorito)
#alternativa
print("my favourite band is", miGrupoFavorito) #la coma agrega un espacio entre las concatenaciones

num1 = "1"
num2 = "2"

print( num1 + num2, "<- Concatena")
print( int(num1) + int(num2), "<- Casteo")

miVariable = False
print(miVariable)
miVariable = 3 > 4
print(miVariable)

if miVariable:
        print("\nverdadero")
else:
        print("\nfalso")