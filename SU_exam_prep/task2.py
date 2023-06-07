data = list(map(int, input().split(' ')))
command = input()

while command != "end":
    if command == "decrease":
        data = list(map(lambda a: a-1, data))
    else:
        explode = command.split(' ')
        current_command = explode[0]
        first_idx = int(explode[1])
        second_idx = int(explode[2])
        if current_command == "swap":
            data[first_idx], data[second_idx] = data[second_idx], data[first_idx]
        else:
            given_num = data[first_idx] * data[second_idx]
            data[first_idx] = given_num

    command = input()
data = list(map(str, data))
output = ", ".join(data)
print(output)


