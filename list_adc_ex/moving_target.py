def shoot_action(number, data, value):
    if -1 < number < len(data):
        data[number] -= value
        if data[number] <= 0:
            data.remove(data[number])

def add_action(number, data, value):
    if -1 < number < len(data):
        data.insert(number, value)
    else:
        print('Invalid placement!')

def strike_action(number, data, value):
    to_remove_lst = []
    if -1 < (number - value) and (number + value) < len(data):
        for i in range(number - value, number + value +1):
            to_remove_lst.append(data[i])
        for i in to_remove_lst:
            data.remove(i)
    else:
        print('Strike missed!')



data = list(map(int, input().split(' ')))
command = input()

while command != 'End':
    current_command = command.split(' ')
    action_adc = current_command[0]
    number_adc = int(current_command[1])
    value_adc = int(current_command[2])

    if action_adc == "Shoot":
        shoot_action(number_adc, data, value_adc)
    if action_adc == "Add":
        add_action(number_adc, data, value_adc)
    if action_adc == "Strike":
        strike_action(number_adc, data, value_adc)


    command = input()

lst = map(str, data)
print('|'.join(lst))
