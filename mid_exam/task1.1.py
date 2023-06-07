biscuits_per_worker = int(input())
number_of_workers = int(input())
enemy_biscuits_count = int(input())

total_count = 0

for i in range(1, 31):
    if i % 3 == 0:
        bisc_per_day = int((biscuits_per_worker * number_of_workers) * 0.75)
        total_count += bisc_per_day
    else:
        total_count += biscuits_per_worker * number_of_workers
print(f"You have produced {total_count} biscuits for the past month.")
diff = abs(total_count - enemy_biscuits_count)
percentage = (diff/enemy_biscuits_count) * 100

if enemy_biscuits_count > total_count:
    print(f"You produce {percentage:.2f} percent less biscuits.")
else:
    print(f"You produce {percentage:.2f} percent more biscuits.")
