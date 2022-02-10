import psycopg2

connection = psycopg2.connect(
                            user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db'
)

print(connection)
try:
    with connection:
            with connection.cursor() as cursor:

                cursor = connection.cursor()  # el cursor nos permite ejecutar sentencias sql
                sentence = 'SELECT * FROM persons where id_person = %s'  # el %s es un placeholder para cargar la id x variable

                id_persona = 2

                cursor.execute(sentence, (id_persona,))  # aca se ejectura la sentencia
                registry = cursor.fetchall()  # con fetchall() se recuperan todos los registros (rows) resultado de la ejecucion de
                                             # la query

except Exception as e:
    print(e)


print(registry)  # cada row se guarda en una tupla y las tuplas se guardan en una lista

#connection.close() # cierran la conexion a la db

# try:
#     with connection:
#             with connection.cursor() as cursor:
#
#                 sentence = 'INSERT INTO persons(name, last_name, email) VALUES(%s, %s, %s)'  # name, last_name, email
#                 values = (
#                     ('Marcos', 'cantu', 'mcantu@mail.com'),
#                     ('angle', 'quintana', 'aquintana@mail.com'),
#                     ('maria', 'gonzales', 'mgonzales@mail.com')
#                 )
#                 cursor.executemany(sentence, values)
#
#                 inserts = cursor.rowcount
#
#                 print(inserts)
#                 print('asd')
#
# except Exception as e:
#     print(e)
# finally:
#     connection.close()

try:
    with connection:
            with connection.cursor() as cursor:

                sentence = 'UPDATE persons SET name = %s, last_name = %s, email = %s where id_person = %s'  # name, last_name, email

                values = ('juan carlos', 'juarez', 'jcjuarez@mail.com', '1')

                # para modificar varios la modificacion es la misma que para insertar
                # se deben agregar todos los values a modificar y cambiar a executemany()
                cursor.execute(sentence, values)

                updates = cursor.rowcount

                print(updates)
                print('asd')

except Exception as e:
    print(e)
finally:
    connection.close()

try:
    with connection:
            with connection.cursor() as cursor:

                

                cursor.execute(sentence, values)

                updates = cursor.rowcount

                print(updates)
                print('asd')

except Exception as e:
    print(e)
finally:
    connection.close()