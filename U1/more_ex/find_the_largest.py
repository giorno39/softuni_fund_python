number = input()
lst = []
for i in number:
    lst.append(i)

lst.sort(reverse=True)
print(''.join(lst))
