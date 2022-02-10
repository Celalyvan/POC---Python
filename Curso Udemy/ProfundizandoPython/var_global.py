var_global = 'variable global'


def print2():
    global var_global  # necesario anteponer globar para modificar variables globales

    var_global='nuevo valor global'


print(var_global)
print2()
print(var_global)

# nonglobal

def asd():
    variable_local_externa = 'variable_local_externa'

    def nested():
        var_local_nested = 'var_local_nested'

        nonlocal variable_local_externa  # permite modificar una variable de un scope superior
        variable_local_externa = 'nuevo valor variable_local_externa'

    nested()

    print(variable_local_externa)

asd()



