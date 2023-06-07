n = int(input())
for i in range(1, n+1):
    working_number = i
    digit_sum = 0
    while working_number > 0:
        digit_sum += working_number % 10
        working_number = working_number // 10
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')







