biscuit_per_worker = int(input())
count_of_workers = int(input())
competing_factory_bisc = int(input())

production_per_day = biscuit_per_worker * count_of_workers

normal_days = production_per_day * 20
third_day = int((production_per_day * 10) * 0.75)
total_biscuits_per_month = normal_days + third_day

diff = abs(competing_factory_bisc - total_biscuits_per_month)
percentage = (diff / competing_factory_bisc) * 100

print(f"You have produced {total_biscuits_per_month} biscuits for the past month.")
if total_biscuits_per_month > competing_factory_bisc:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
