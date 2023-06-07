a,b = int(input()), int(input())

courses = a // b
if a % b != 0:
    courses += 1
print(courses)
