number_of_electrons = int(input())
counter = 1
lst = []

while number_of_electrons >= 2 * counter ** 2:
    lst.append(2 * counter ** 2)
    number_of_electrons -= 2 * counter ** 2
    counter += 1
if number_of_electrons != 0:
    lst.append(number_of_electrons)

print(lst)


