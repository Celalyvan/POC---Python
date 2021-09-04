class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.name + other.name

    def __sub__(self, other):
        return self.age - other.age


person1 = Person('Juan', 20)
person2 = Person('Maria', 21)

print(person1 + person2)
print(person1 - person2)