command = input()
total_price = 0

while command != "regular" and command != "special":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    final_price = taxes + total_price
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if command == "regular":
        print(f"Total price: {final_price:.2f}$")
    else:
        discount_price = final_price * 0.9
        print(f"Total price: {discount_price:.2f}$")

