counter = 0

while True:
    work_to_do = input()
    if work_to_do == 'dog' or work_to_do == 'cat' or work_to_do == 'coding' or work_to_do == 'movie':
        counter += 1
    elif work_to_do == 'DOG' or work_to_do == 'CAT' or work_to_do == 'CODING' or work_to_do == 'MOVIE':
        counter += 2
    elif work_to_do == 'END':
        break

if counter > 5:
    print('You need extra sleep')
else:
    print(counter)
