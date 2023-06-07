def foo(num):
    if num == num[::-1]:
        return True
    else:
        return False

numbers = input().split(', ')

for i in numbers:
    print(foo(i))
