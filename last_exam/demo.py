import string as validation

data = input()

counter = 0
for i in data:
    if i in validation.ascii_letters or i in validation.digits or i in "_":
        counter += 1
if counter != len(data):
    print("Password must consist only of letters, digits and _!")