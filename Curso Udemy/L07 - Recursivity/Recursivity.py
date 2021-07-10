def factorial(num):
    if num ==1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(4))

def imprDesc(num):

    if num >= 1:
        print(num)
        return imprDesc(num-1)

imprDesc(8)