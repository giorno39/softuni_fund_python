data = input().split(' ')
even_lengths = list(filter(lambda word: len(word) % 2 == 0, data))

for i in even_lengths:
    print(i)
