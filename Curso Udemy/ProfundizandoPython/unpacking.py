v1 = 1,2,3
print(v1)

v1, v2, v3 = 1,2,3
print(v1,v2,v3)

v1,v2, *v3 = 1,2,3,4,5,6,7,8,9  # anteponiendo el * a v3 indicamos que va a tomar los valores restantes
print(v1,v2,v3)
