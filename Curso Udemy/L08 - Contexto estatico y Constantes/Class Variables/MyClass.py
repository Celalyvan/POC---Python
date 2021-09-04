class MyClass:
    class_variable = 'class var value'  # static atribute, shared between all objects of this class

    def __init__(self, class_instance):
        self.class_instance = class_instance

    @staticmethod
    def static_method():
        print(MyClass.class_variable)

    @classmethod
    def class_method(cls):
        print(cls.class_variable)

    def instance_method(self):
        self.class_method()
        self.static_method()
        print(self.class_instance)

print(MyClass.class_variable)

myclass = MyClass('variable instancia')
print(myclass.class_variable)
print(myclass.class_instance)

MyClass.static_method()

MyClass.class_method()

myObject1 = MyClass('object variable')
print('asd')
myObject1.instance_method()
