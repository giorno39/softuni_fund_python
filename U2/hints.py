n = int(input())
counter = 0
if n % 2 == 0:
    counter += 1
if n % 3 == 0:
    counter += 1
if n % 4 == 0:
    counter += 1
if n % 5 == 0:
    counter += 1
if n % 6 == 0:
    counter += 1
if n % 7 == 0:
    counter += 1
if n % 8 == 0:
    counter += 1
if n % 9 == 0:
    counter += 1
if counter <= 1:
    print(True)
else:
    print(False)
