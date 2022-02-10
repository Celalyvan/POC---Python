from logger_base import log
from connection import Connection

class CursorPool:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('start __enter__')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()

        return self._cursor

    def __exit__(self, exception_type, exception_val, exception_traceback):
        log.debug('executing __exit__')
        if exception_val:
            self._connection.rollback()
            log.error(f'error: {exception_val} {exception_traceback}')
        else:
            self._connection.commit()
            log.debug('commited')
        self._cursor.close()
        Connection.freeConnection(self._connection)


if __name__ == '__main__':
    with CursorPool() as cursor:
        cursor.execute('SELECT * FROM persons')
        log.debug(cursor.fetchall())
