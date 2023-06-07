def length_check(data):
    if len(data) < 8:
        return "Password must be at least 8 characters long!"


def content_check(data):
    counter = 0
    for i in data:
        if i in validation.ascii_letters or i in validation.digits or i in "_":
            counter += 1
    if counter != len(data):
        print("Password must consist only of letters, digits and _!")


def uppercase_check(code):
    counter = 0
    for i in code:
        if i in validation.ascii_uppercase:
            counter += 1
    if counter == 0:
        return "Password must consist at least one uppercase letter!"


def lowercase_check(code):
    counter = 0
    for i in code:
        if i in validation.ascii_lowercase:
            counter += 1
    if counter == 0:
        return "Password must consist at least one lowercase letter!"


def digit_check(code):
    counter = 0
    for i in code:
        if i in validation.digits:
            counter += 1
    if counter == 0:
        return "Password must consist at least one digit!"


import string as validation

password = input()
new_password = password

while True:
    command = input()
    if command == "Complete":
        break

    explode = command.split(" ")
    type_of_command = explode[0]
    if type_of_command == "Make":
        type_of_remaking = explode[1]
        idx = int(explode[2])
        if type_of_remaking == "Upper":
            new_password = password[:idx] + password[idx].upper() + password[idx + 1:]
            password = new_password
            print(new_password)
        elif type_of_remaking == "Lower":
            new_password = password[:idx] + password[idx].lower() + password[idx + 1:]
            password = new_password
            print(new_password)
    if type_of_command == "Insert":
        idx = int(explode[1])
        letter = explode[2]
        if idx < len(new_password):
            new_password = password[:idx] + letter + password[idx:]
            password = new_password
            print(new_password)
    if type_of_command == "Replace":
        char = explode[1]
        value = int(explode[2])
        if char in password:
            new_value = ord(char) + value
            new_char = chr(new_value)
            new_password = password.replace(char, new_char)
            password = new_password
            print(new_password)

    if type_of_command == "Validation":
        if length_check(new_password) is not None:
            print(length_check(new_password))
        if content_check(new_password) is not None:
            print(content_check(new_password))
        if uppercase_check(new_password) is not None:
            print(uppercase_check(new_password))
        if lowercase_check(new_password) is not None:
            print(lowercase_check(new_password))
        if digit_check(new_password) is not None:
            print(digit_check(new_password))

