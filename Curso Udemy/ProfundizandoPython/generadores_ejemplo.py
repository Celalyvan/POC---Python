def numgen():
    for numero in range(1,6):
        yield numero


gen = numgen()
for valor in gen:
    print(valor)

gen = numgen() # reseteamos el generador


while True:
    try:
        print(next(gen))
    except StopIteration as e:
        print(f'finalizo el generador: {e}')
        break