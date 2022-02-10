# coleccion mutable de elementos unicos, pero sus elementos
# deben ser inmutables (strings, booleans, floats, tuplas)

# para crear un set vacio
cjto = set()

# mutabilidad
cjto.add('juan')
print(cjto)

#valores unicos
cjto.add('juan')
print(cjto)


# creando set a partir d eun iterable
cjto = set([4, 5, 7, 8, 4])
print(cjto)

# agregando de un set
cjto2 = {101, 200, 300, 300}
print(cjto2)

cjto.update(cjto2)
print(cjto)

# shallow copy

cjto_cpy = cjto.copy()
print(cjto_cpy)


# metodos de sets:
    # set.union(set2)         - (si(si)si)
    # set.interseccion(set2)  - (no(si)no)
    # set.difference(set2)    - el solo de set (si(no)no)

# set contenido en otro
    # set.issubset(set2)
    # set.issuperset()
    # set.isdisjoint()   -  no hay relacion entre set y set2
