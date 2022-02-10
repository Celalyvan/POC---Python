from cursor_pool import CursorPool
from logger_base import log
from user import User


class UserDAO:

    _SELECT = 'SELECT * FROM users ORDER BY id_user'
    _INSERT = 'INSERT INTO users ( username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE users SET username = %s, password=%s WHERE id_user=%s'
    _DELETE = 'DELETE FROM users WHERE id_user=%s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            log.debug('selecting users')
            cursor.execute(cls._SELECT)

            registries = cursor.fetchall()
            users = []

            for registry in registries:
                user = User(registry[0], registry[1], registry[2])
                users.append(user)

            return users


    @classmethod
    def insert(cls, user):
        with CursorPool() as cursor:
            log.debug(f'user to insert: {user}')
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)

    @classmethod
    def update(cls,user):
        with CursorPool() as cursor:
            log.debug(f'user to update: {user}')
            values = (user.username, user.password, user.id_user)
            cursor.execute(cls._UPDATE, values)


    @classmethod
    def delete(cls, user):
        with CursorPool() as cursor:
            log.debug(f'user to delete: {user}')
            values = (user.id_user,)
            cursor.execute(cls._DELETE, values)


if __name__ == '__main__':
    for user in UserDAO.select():
        log.debug(user)

    user1 = User(username='tomas', password=123)

    UserDAO.insert(user1)

