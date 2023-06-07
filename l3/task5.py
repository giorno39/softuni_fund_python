n = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)

type_of_numbers = input()
print(eval(type_of_numbers))

