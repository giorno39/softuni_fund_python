lst = []

while True:
    x = input()
    if x == '\end':
        break
    else:
        lst.append(int(x))

lst1 = [] #четни
lst2 = [] #нечетни

for x in lst:
    if x % 2 == 0:
        lst1.append(x)
    elif x % 3 == 0:
        lst2.append(x)

even_sum = sum(lst1)
odd_sum = sum(lst2)
mean_even = even_sum/len(lst1)
men_odd = odd_sum / len(lst2)
min_even = min(lst1)
max_even = max(lst1)
min_odd = min(lst2)
max_odd = min(lst2)
print(eval(input()))
