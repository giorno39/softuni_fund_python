n = int(input())
counter = 0
is_it_balanced = False
for _ in range(n):
    symbol = input()
    if symbol == '(':
        counter += 1
    if counter == 1:
        counter += 1
        continue
    if counter == 2:
        counter = 0
        if symbol == ')':
            is_it_balanced = True
        else:
            is_it_balanced = False

if is_it_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

