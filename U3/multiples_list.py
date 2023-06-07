first_number = int(input())
seconds_number = int(input())
lst = []

for i in range(1, seconds_number +1):
    current_number = i * first_number
    lst.append(current_number)

print(lst)
