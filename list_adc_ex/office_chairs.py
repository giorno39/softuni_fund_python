k = int(input())
condition = True
chairs_left = 0
for i in range(1, k + 1):
    data = input().split(' ')
    chairs_in_room = data[0]
    persons_in_room = int(data[1])



    diff = abs(len(chairs_in_room) - persons_in_room)

    if len(chairs_in_room) < persons_in_room:
        print(f'{diff} more chairs needed in room {i}')
        condition = False
    elif len(chairs_in_room) > persons_in_room:
        chairs_left += diff

if condition:
    print(f'Game On, {chairs_left} free chairs left')



