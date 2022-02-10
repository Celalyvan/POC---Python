from connection import Connection
from cursor_pool import CursorPool
from person import Person
from logger_base import log

class PersonaDAO:
    _SELECT = 'SELECT * FROM persons ORDER BY id_person'
    _INSERT = 'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE persons SET name = %s, last_name = %s, email = %s WHERE id_person = %s'
    _DELETE = 'DELETE FROM persons WHERE id_person=%s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:

            cursor.execute(cls._SELECT)
            registries = cursor.fetchall()
            people=[]

            for registry in registries:
                person = Person(registry[0], registry[1],registry[2],registry[3])
                people.append(person)

            return people

    @classmethod
    def insert(cls, person):
        with CursorPool() as cursor:
            values = (person.name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'inserted person: {person}')

    @classmethod
    def update(cls, person):
        with CursorPool() as cursor:
            values = (person.name, person.last_name, person.email, person.id_person)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'updated person: {person}')

    @classmethod
    def delete(cls, person):
        with CursorPool() as cursor:
            values = (person.id_person,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'deleted person: {person}')

if __name__ == '__main__':

    #select *
    people = PersonaDAO.select()
    for person in people:
        log.debug(person)
    #insert
    # person1 = Person(name='peter', last_name='languila', email='pnajera@mail.com')
    # PersonaDAO.insert(person1)

    #update
    # person1 = Person(name='juancho', last_name='longaniza', email='pnajera@mail.com',id_person=16)
    # PersonaDAO.update(person1)

    #update
    person1 = Person(id_person=20)
    PersonaDAO.delete(person1)


