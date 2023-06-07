data = list(map(int, input().split(', ')))

even = [str(num) for num in data if num % 2 == 0]
odd = [str(num) for num in data if num % 2 != 0]
negatives = [str(num) for num in data if num < 0]
positives = [str(num) for num in data if num >= 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
