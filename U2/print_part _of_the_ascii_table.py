first_number, second_number = int(input()), int(input())

for i in range(first_number, second_number + 1):
    symbol = chr(i)
    print(symbol, end=' ')
