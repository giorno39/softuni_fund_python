data = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())

for route in data:
    if route == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    explode = route.split(" ")
    command = explode[0]
    num = int(explode[1])
    if command == "Travel":
        if starting_fuel >= num:
            starting_fuel -= num
            print(f"The spaceship travelled {num} light-years.")
        else:
            print("Mission failed.")
            break
    if command == "Enemy":
        if starting_ammunition >= num:
            starting_ammunition -= num
            print(f'An enemy with {num} armour is defeated.')
        else:
            if num * 2 <= starting_fuel:
                print(f"An enemy with {num} armour is outmaneuvered.")
                starting_fuel -= num * 2
            else:
                print("Mission failed.")
                break
    if command == "Repair":
        starting_ammunition += num * 2
        starting_fuel += num
        print(f"Ammunitions added: {num * 2}.")
        print(f"Fuel added: {num}.")


