# set

planetas = {'marte', 'venus', 'jupiter'}

print(planetas)

# largo
print(len(planetas))

# revisar existencia

print('marte' in planetas)  # puede usarse en lista y tupla, distingue mayus

# agregar elem

planetas.add('Tierra')

print(planetas)

# eliminar elem

planetas.discard('Tierra')  # se puede usar discard que no tira error si el elemento no se encuentra en la lista

print(planetas)

# vaciar el set
planetas.clear()

print(planetas)
# borrar planetas
del planetas

print(planetas)