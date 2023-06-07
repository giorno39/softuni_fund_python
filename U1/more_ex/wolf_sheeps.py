x = input()
lst = x.split(', ')
counter = 0
if lst[len(lst)-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    lst2 = lst[::-1]
    for i in lst2:
        counter += 1
        if i == 'wolf':
            print(f'Oi! Sheep number {counter-1}! You are about to be eaten by a wolf!')

