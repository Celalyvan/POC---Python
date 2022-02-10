from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclass(eq=True, frozen=True)  # genera automaticamente metodo init y repr
# eq => equals
# frozen => hace/deshace inmutables a los objetos
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_persona: ClassVar[int] = 0  # variable de clase

    # validar valores asignados a los atributos

    def __post_init__(self): #aca es donde se hacen las validaciones
        if not self.nombre:
            raise ValueError('valor de nombre vacio')
        if not self.apellido:
            raise ValueError('valor de nombre vacio')


persona1 = Persona('juan', 'perez', None)
print(persona1)
persona2 = Persona('karla', 'gomez', Domicilio('saturno',15))
print(persona2)
print(f'variable de clase: {Persona.contador_persona}')
persona3 = Persona('karla', 'gomez', Domicilio('saturno',15))
print(f' igual persona2 a persona3? {persona2==persona3}')
collection = {persona1, persona2}
print(collection)



