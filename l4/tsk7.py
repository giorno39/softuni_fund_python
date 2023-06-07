vasko = input().split(' ')
lst1 = []

def foo(lst):
    for i in lst:
        x = round(float(i))
        lst1.append(x)
    return lst1

print(foo(vasko))
