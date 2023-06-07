data = input().split(", ")
command = input()

while command != "End":
    explode = command.split(" - ")
    current_command = explode[0]
    current_phone = explode[1]

    if current_command == "Add":
        if current_phone not in data:
            data.append(current_phone)
    elif current_command == "Remove":
        if current_phone in data:
            data.remove(current_phone)
    elif current_command == "Bonus phone":
        phones = current_phone.split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if old_phone in data:
            idx = data.index(old_phone) + 1
            data.insert(idx, new_phone)
    elif current_command == "Last":
        if current_phone in data:
            data.remove(current_phone)
            data.append(current_phone)

    command = input()

output = ", ".join(data)
print(output)
