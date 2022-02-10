from logger_base import log


class Person:
    def __init__(self, id_person=None, name=None, last_name=None, email=None):
        self._id_person = id_person
        self._name= name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return f'''
                id: {self.id_person}, Name: {self.name},
                Last name: {self.last_name}, Email: {self.email}
        '''

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        self._id_person = id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name



    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    person1 = Person(1, 'juan', 'perez', 'jperez@mail.com')
    log.debug(person1)

    person1 = Person( name='juan', last_name='perez', email='jperez@mail.com')
    log.debug(person1)
