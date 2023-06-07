def odd_or_even(lst):
    even_nums = []
    odd_nums = []
    for i in lst:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)

    print(f'Odd sum = {sum(odd_nums)}, Even sum = {sum(even_nums)}')


numbers = map(int, list(input()))
odd_or_even(numbers)
