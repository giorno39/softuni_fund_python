lines = int(input())
best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for _ in range(lines):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality

    if best_value < value:
        best_value = value
        best_weight = weight
        best_time = time
        best_quality = quality

print(f'{best_weight} : {best_time} = {best_value:.0f} ({best_quality})')
