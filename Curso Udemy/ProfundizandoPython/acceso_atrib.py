class MiClase:
    def __init__(self, public, protected, private):
        self.public = public
        self._protected = protected
        self.__private = private
# en python todavia es posible acceder a estos atributos pese a q sea mala practica
# este mismo criterio de privacidad aplica para metodos
# pero si queremos acceder a un atributo privado lanza excepcion


