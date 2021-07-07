string = 'Holanda'

for letter in string:
    print(letter)
    if letter == 'a':
        break  # funciona como en Java
else:
    print("end of For")

# for i in range(6):  # el comun fori
#     if i%2 == 0:
#         print(f'Value: {i}')

for i in range(6):
    if i % 2 !=0:
        continue  # interrumpe esta iteracion y pasa a la siguiente
    print(f'Value: {i}')

