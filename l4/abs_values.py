numbers = input().split(' ')
lst = []
def foo():
    for i in numbers:
        current_number = abs(float(i))
        lst.append(current_number)
    return lst

print(foo())


