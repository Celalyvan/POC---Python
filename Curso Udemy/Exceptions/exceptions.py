from SameNumberException import SameNumberException

result = None

a2= '10'


try:

    a = int(input('1st nmbr '))
    b = int(input('2nd nmbr '))
    if a==b:
        raise SameNumberException('same numbers')
except ZeroDivisionError as e:
    print(f' Error: {e}, {type(e)}')
except TypeError as e:
    print(f' Error: {e}, {type(e)}')
except Exception as e:
    print(f' Error: {e}, {type(e)}')
else:
    result=a/b
    print('no exceptions recorder')
finally:
    print('finally block')


print(f'resul = {result}')
print('continue...')