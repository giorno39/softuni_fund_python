word1 = input()
word2 = input()

for i in range(len(word1)):
    if word1[i] != word2[i]:
        replacement = word2[i]
        word3 = word1[0:i] + replacement + word1[i+1:]
        word1 = word3
        print(word1)
