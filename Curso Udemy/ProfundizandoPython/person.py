class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'name: {self.name}, apellido: {self.last_name},id: {hex(id(self)).upper()}'



person1 = Person('juan', 'camilez')
print(person1)