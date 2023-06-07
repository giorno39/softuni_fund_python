first_number = int(input())
seconds_number = int(input())
third_number = int(input())

if first_number >= seconds_number and first_number >= third_number:
    largest_number = first_number
elif seconds_number >= first_number and seconds_number >= third_number:
    largest_number = seconds_number
else:
    largest_number = third_number

print(largest_number)


