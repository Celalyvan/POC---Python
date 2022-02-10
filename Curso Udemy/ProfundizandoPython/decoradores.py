# funciones q reciben y regresan funciones
# se usa para extender funcionalidad

# 1-fuincion decorador
# 2-fimcopm a decprar
# 3- funcion decorada

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):  # remover *args, **kwargs para descomentar lo de abajo
        print('antes de ejecutar funcion')
        resultado = funcion_a_decorar_b(*args, **kwargs)  # remover *args, **kwargs para descomentar lo de abajo
        print('despues de ejecutar funcion')
        return resultado



    return funcion_decorada_c

#
# @funcion_decorador_a
# def mostrar_mensaje():
#     print('hola desde mostrar_mensaje')
#
#
# mostrar_mensaje()
#
#
# print('\n')
#
# @funcion_decorador_a
# def imprimir():
#     print('desde imprimir')
#
# imprimir()


@funcion_decorador_a
def sumar(a,b):
    return a+b


print(f'resultado de sumar con decorador: {sumar(5,3)}')
