lines = int(input())
capacity = 0
for _ in range(lines):
    water = int(input())
    if capacity + water <= 255:
        capacity += water
    else:
        print('Insufficient capacity!')
print(capacity)
