# Calcular area y perimetro de un rectangulo
# Tomar alto y ancho por teclaedo, y reportar resultados

alto = int(input("proporcione el alto "))
ancho = int(input("proporcione el ancho "))

area = alto * ancho
perimetro = alto * 2 + ancho * 2

print(f'Area = {area}')
print(f'Perimetro = {perimetro}')
