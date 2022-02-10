# conservan un orden unlike sets
# las llaves son keysensitive

dicc = {'nombre' : 'juan', 'apellido':'perez','edad':23}

print(dicc)

# los diccionarios pueden mutar pero no las llaves
    # no se pueden usar listas como keys, pero si tuplas

# acceder a un value a travez de una key
print(dicc['nombre'])  # si la key no existe lanza una excepcion

    # otra forma
print(dicc.get('nombre', 'no se encontro la key'))  # si la key no existe lanza el mensaje en caso de no encontrarlo
print(dicc.get('asd', 'no se encontro la key'))

# setdefault agrega valores default a las keys
name = dicc.setdefault('nombre', 'default value')
print(name)
print(dicc)
name = dicc.setdefault('nombres', 'default value')
print(name)
print(dicc)

# imprimir con pprint
from pprint import pprint as pp

pp(dicc, sort_dicts=False)

