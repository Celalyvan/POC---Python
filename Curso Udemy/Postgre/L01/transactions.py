import psycopg2 as db

connection = db.connect(
                            user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db'
)

print(connection)
try:

    connection.autocommit = False  # cancela el auto guardado de datos

    cursor = connection.cursor()
    sentence = 'INSERT INTO persons (name, last_name, email) VALUES (%s,%s,%s)'
    values = ('maria', 'sparza', 'msparza@mail.com')

    cursor.execute(sentence, values)

    connection.commit()

    print('asd')

except Exception as e:
    connection.rollback()
    print(e)


#print(registry)