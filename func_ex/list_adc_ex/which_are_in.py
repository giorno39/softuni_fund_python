first_lst = input().split(', ')
second_lst = input().split(', ')

final_lst = []

for i in first_lst:
    for k in second_lst:
        if i in k:
            if i in final_lst:
                pass
            else:
                final_lst.append(i)

print(final_lst)