array = [8, 3, 5, 2, 6]


def partition(numbers, low, high):
    i = low
    j = high
    indice = (int((low + high) / 2))
    pivot = numbers[indice]

    while i <= j:
        while (numbers[i] < pivot):
            i += 1

        while (numbers[j] > pivot):
            j -= 1

        if (i <= j):
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
            i += 1
            j -= 1

    return i


def sortCustom(numbers, low, high):
    index = partition(numbers, low, high)
    print(numbers)
    if (low < index - 1):
        sortCustom(numbers, low, index - 1)

    if (index < high):
        sortCustom(numbers, index, high)


print("antes sort")
print(array)
sortCustom(array, 0, len(array) - 1)
print("desp sort")
print(array)
