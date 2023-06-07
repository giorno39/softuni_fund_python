type_of_operation = input()
a = int(input())
b = int(input())

def multiply(a, b):
    return a * b

def divide(a,b):
    return int(a/b)

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b


print(eval(type_of_operation)(a, b))
