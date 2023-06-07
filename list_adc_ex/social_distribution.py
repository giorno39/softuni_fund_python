data = list(map(int, input().split(', ')))
k = int(input())
low_wealth = [num for num in data if num < k]
high_wealth = [num for num in data if num > k]
if len(low_wealth) == len(high_wealth):
    pass
else:
    print(f'No equal distribution possible')