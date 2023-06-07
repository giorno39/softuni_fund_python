data = list(map(int, input().split("@")))

command = input()
idx = 0

while command != 'Love!':
    explosion = command.split(' ')
    number = int(explosion[1])
    idx = (idx + number) % (len(data) - 1)
    if data[idx] != 0:
        data[idx] -= 2
        if data[idx] == 0:
            print(f"Place {idx} has Valentine's day.")
    if data[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")
    command = input()

print(f"Cupid's last position was {idx}.")
if sum(data) == 0:
    print("Mission was successful.")
else:
    counter = 0
    for i in data:
        if i != 0:
            counter += 1
    print(f'Cupid has failed {counter} places.')

# print(f'Cupid has failed 3 places.')