n = int(input())
total_price = 0

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price_per_day = price_per_capsule*days*capsule_count
    print(f'The price for the coffee is: ${price_per_day:.2f}')
    total_price += price_per_day
print(f'Total: ${total_price:.2f}')

