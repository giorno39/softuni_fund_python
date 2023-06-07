lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
aureus = 0
counter = 0
for loses in range(1, lost_fights + 1):
    if loses % 2 == 0:
        aureus += helmet_price

    if loses % 3 == 0:
        aureus += sword_price
        if loses % 2 == 0:
            aureus += shield_price
            counter += 1
            if counter == 2:
                aureus += armor_price
                counter = 0


print(f'Gladiator expenses: {aureus:.2f} aureus')
