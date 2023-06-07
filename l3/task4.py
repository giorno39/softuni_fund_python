n = int(input())
key_word = input()
lst = []
filtered_lst = []

for _ in range(n):
    current_word = input()
    lst.append(current_word)
    if key_word in current_word:
        filtered_lst.append(current_word)
print(lst)
print(filtered_lst)
