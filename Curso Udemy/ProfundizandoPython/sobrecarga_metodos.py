# simular sobrecarga deconstructores

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return f'Nombre: {self.nombre}, apellido: {self.apellido}'

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None) # llama al metodo __init__ indirectamente



persona_vacia = Persona.crear_persona_vacia()
print(persona_vacia)

