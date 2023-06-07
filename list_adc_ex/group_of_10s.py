data = list(map(int, input().split(", ")))
tens = 10
to_remove_list = []

while data:
    current_list = list(filter(lambda num: num <= tens, data))
    for i in current_list:
        data.remove(i)

    print(f"Group of {tens}'s: {current_list}")
    tens += 10











