# permiten trasnformar de manera programatica nuestra clase
# similar a los de funciones (metaprogramacion)
import inspect


def decorador_repr(cls):
    print('ejecutando decorador')
    print(f'objeto clase: {cls.__name__}')

    atributos = vars(cls)
    for nombre,atributo in atributos.items():
        print(nombre,atributo)

    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no sobreescribio __init__' )

    firma_init = inspect.signature(cls.__init__)  # recupera los parametros del metodo pasado por parametro
    print(f'firma metodo __init__: {firma_init}')
    # extraemos el self de la firma
    parametros_init = list(firma_init.parameters)[1:]
    print(f'parametros metodo __init__: {parametros_init}')

    # revisamos si existe un property para cada parametro
    for parametro in parametros_init:
        is_metodo_property = isinstance(atributos.get(parametro), property)
        if not is_metodo_property:
            raise TypeError(f'no hay property para parametro: {parametro}')

    # creando repr dinamicamente
    def metodo_repr(self):
        nombre_clase = self.__class__.__name__

        # para atributos usamos expresion generadora
        generador_args = (f'{nombre} = {getattr(self, nombre)!r}' for nombre in parametros_init)

        lista_args = list(generador_args)
        print(lista_args)

        #creamos el retorno
        argumentos = ', '.join(lista_args)
        print(argumentos)

        #creamos el retorno
        retorno = f'{nombre_clase}({argumentos})'

        return retorno

    setattr(cls, '__repr__', metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('constructor')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido



persona1 = Persona('juan' , 'perez')
persona2 = Persona('karla', 'gomez')

print('listado personas ')
print(persona1)
print(persona2)

print(inspect.getsource(persona2.__repr__))
