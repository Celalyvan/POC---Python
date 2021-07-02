myVariable = 10
print(myVariable)

myVariable = myVariable + 1  # increases myVariable value by 1

print(myVariable)

myVariable += 1  # also increases myVariable value by 1
print(myVariable)

# this operators are usable with any other arithmetical operation

myVariable /= 5

print(myVariable)

# comparison operators

a = 3
b = 3

result = (a == b)  # a equals b

print(result)

result = a != b  # a different than b

# <, >, <= & >= work the same as Java

# LOGIC OPERATORS   & == and, | == or, ! == not
a = True
b = False

c = a & b  # c = a and b works the same

print("truth value", c)

c = a or b  # c = a | b works the same

print("truth value", c)

#value in range

value = int(input("insert number "))
minValue = 0
maxValue = 5

range = value >= minValue and value <= maxValue

if range:
    print('in range')
else:
    print("out of range")


