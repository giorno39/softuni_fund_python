key = int(input())
z = int(input())
lst = []
for _ in range(z):
    symbol = input()
    n_value = ord(symbol)
    new_symbol = chr(key + n_value)
    lst.append(new_symbol)

print(''.join(lst))
