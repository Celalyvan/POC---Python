#las modificaciones a los strings generan nuevas instanciaciones
#en memoria xq son inmutables

message = 'hello' + ' world'
print(message)

message = 'hello'  ' world'
print(message)

#  message2 = 'bye' message ERROR

message += ' another append'
print(message)

message = 'palabraSinCaps'
print(message.capitalize())

tuple_str= ('hola','mundo','soy', 'tomas')
message = ' '.join(tuple_str)
print(message)

lista_cursos=['java', 'python', 'Angular', 'Spring']
message= ', '.join(lista_cursos)
print(message)

string= 'HolaMundo'
message= '.'.join(string)
print(message)

cursos = 'java python jss angular spring'

lista_cursos = cursos.split()
print(lista_cursos)

cursos = 'java,python,js,angular,spring'

lista_cursos = cursos.split()
print(f'split sin parametros {lista_cursos}')
lista_cursos = cursos.split(',')
print(f'split CON parametros {lista_cursos}')
lista_cursos = cursos.split(',', 2)
print(f'split generando 2 separaciones {lista_cursos}')

print( '\n\n==============  Formating  ==============\n')

name = 'juan'
age = 25
message = 'My name is %s, my age %d'%(name, age)
print(message)

data = ('karla', 'Gomez', 'kgomez@mail.com')
message = '''
            name:........%s
            last name:...%s
            mail:........%s'''%data
print(message)

data = ('karla', 'Gomez', 'kgomez@mail.com')
message = '''
            name:........%s
            last name:...%s
            mail:........%s'''
print(message%data)

name = 'juan'
age = 28
message = 'name: {} age: {}'.format(name, age)
print(message)


message = 'name: {} age: {}'.format(name, age)
print(message)

name = 'juan'
age = 28
mail = 'jmanes@mail.com'
print(name, age, mail, sep=', ')

print(5*'hello ')

message = 'AAA.'
print(message.isupper())


#alinear strings
message = 'asd'
print('\n'+message.center(90,'-'))

print('\n'+message.center(len(message)+20,'='))

print(message.ljust(50,'='))  # texto a la izquierda, el resto rellenado con el caracter

print(message.rjust(50,'='))  # texto a la derecha, el resto rellenado con el caracter


#reemplazar chars
print(' reemplazo '.center(60, '_'))

message = 'este es el mensaje donde quiero reemplazar caracteres'
print(message)
print(message.replace(' ', '_'))  # replace(to_be_replaced, the_replace)



message = '***este es el mensaje donde quiero strippear***'
print(message)
print(message.strip('*'))

message = '***este es el mensaje donde quiero L-strippear***'
print(message.lstrip('*'))

message = '***este es el mensaje donde quiero R-strippear***'
print(message.rstrip('*'))
