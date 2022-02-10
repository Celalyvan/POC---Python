from logger_base import log
import sys
from psycopg2 import pool

class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None


    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)

                log.debug(f'pool stablished : {cls._pool}')

                return cls._pool

            except Exception as e:
                log.error(f'error at getting pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'connection recieved : {connection}')

        return connection

    @classmethod
    def freeConnection(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'connection returned: {connection}')

    @classmethod
    def closeConnections(cls):
        cls.getPool().closeall()







if __name__ == '__main__':
   connection1 = Connection.getConnection()
   Connection.freeConnection(connection1)
   connection2 = Connection.getConnection()
   # connection3 = Connection.getConnection()
   # connection4 = Connection.getConnection()
   # connection5 = Connection.getConnection()
   # connection6 = Connection.getConnection()
   #
