def sumTodo(*nums):
    resultado = 0
    for i in nums:
        resultado += i

    return resultado


print(sumTodo(4, 5, 1, 1, 5, 5, 12, 65, 465, 1, 2))


def multTodo(*args):
    result = 1
    for i in args:
        result *= i

    return result


print(multTodo(4, 5, 1, 1, 5, 5, 2, 6, 3, 1, 2))
