data = input().split(', ')
sentence = input()
new_lst = []

for i in data:
    if i in sentence:
        new_lst.append(i)

print(new_lst)
