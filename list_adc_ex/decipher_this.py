data = input().split(' ')

for i in data:
    current_word = [str(num) for num in i if num.isdigit()]
    first_letter = chr(int(''.join(current_word)))
    lst = [str(num) for num in i if not num.isdigit()]
    lst[0], lst[-1] = lst[-1], lst[0]
    lst.insert(0, first_letter)
    print(''.join(lst), end=' ')






