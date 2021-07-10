class Persona:

    def __init__(self, nombre, apellido, edad, *args, **kwargs):  # self == this en Java, el __ (double underscore o dunder)
        self._nombre = nombre # anteponer el _ indicamos q el atributo es privado pero se puede modificar con __ se vuelve privado de verdad
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    @property # nos asegura q podamos acceder a ese atributo SOLO por este metodo, ya que llama indirectamente al metodo
    # ademas que nos limpia el codigo del parentesis vacio persona1.nombre() pasaria a ser persona1.nombre
    def nombre(self): #getter
        return self._nombre

    #  para agregar un setter primero necesito tener creado el getter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido}; Edad {self.edad}; {self.args}, {self.kwargs}\n')


 #   pass  # no se va a procesar nada mas, se va a crear este tipo de dato


persona1 = Persona('Juan', 'perez', 31, '456465465465',2,3,5 , m='manzana', p='pera')
# persona2 = Persona('Karla', 'Gomez', 28)

persona1.mostrar_detalle()
# persona2.mostrar_detalle()

# se pueden agregar atributos on the fly a objetos individuales
persona1.telefono = '4465132165'
persona1.mostrar_detalle()
print(persona1.telefono)
