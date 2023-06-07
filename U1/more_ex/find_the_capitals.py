word = input()
lst = []

for i in range(len(word)):
    if word[i].isupper():
        lst.append(i)
    else:
        continue

print(lst)
