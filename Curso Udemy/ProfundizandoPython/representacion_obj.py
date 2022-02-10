# representacion de objetos (str, repr, format)

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# forma recomendada para entender entre programadores es el metodo de representacion default
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})'
# metodo str orientado a usuario final u otros sistemas
    def __str__(self):
        return f''
# format x default llama a str
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} nombre: {self.nombre}, apellido: {self.apellido} '


persona1 = Persona('juan', 'carlos')
print(persona1)
# o sino
print(f'persona1 es: {persona1!r}')  # de esta forma se llama directamente a repr
print(f'{persona1}')  # de esta forma se llama directamente al metodo format

