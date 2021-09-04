from Employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = departament

    def __str__(self):
        return f'Manager |{self.departament}| {super().__str__()}'

