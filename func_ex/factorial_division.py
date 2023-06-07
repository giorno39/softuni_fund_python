def fact_calc(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i

    return f

num1 = int(input())
num2 = int(input())

result = fact_calc(num1) / fact_calc(num2)

print(f"{result:.2f}")
