from Employee import Employee
from Manager import Manager


def print_details(object):
    print(object)
    print(type(object))
    if isinstance(object, Manager): # instanceOf() in Java
        print('is manager')



employee = Employee('Juan', 20000)
print_details(employee)

manager = Manager('karla', 25000, 'IT')
print_details(manager)
