class Aritmetica:
    """
    Estos comentarios (DocString) sirven para dejar comentarios en lka clase
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(3, 8)

print('suma', aritmetica1.sumar())
print('resta', aritmetica1.restar())
print('multiplicar', aritmetica1.multiplicar())
print(f'dividir {aritmetica1.dividir():.2f}') #indicamos la cantidad de decimales a mostrar
