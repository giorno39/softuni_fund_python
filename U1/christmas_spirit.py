quantity = int(input())
days = int(input())

christmas_spirit = 0
total_cost = 0
fifth_day_conditional = False

for day in range(1, days+1):
    fifth_day_conditional = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        total_cost += 2 * quantity

    if day % 3 == 0:
        total_cost += (5 + 3) * quantity
        christmas_spirit += 13
        fifth_day_conditional = True

    if day % 5 == 0:
        total_cost += quantity * 15
        christmas_spirit += 17
        if fifth_day_conditional:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 5 + 3 + 15
        if day == days:
            christmas_spirit -= 30

print(f'Total cost: {total_cost}')

print(f'Total spirit: {christmas_spirit}')



