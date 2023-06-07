def foo(order, quantity):
    if order == 'coffee':
        return quantity * 1.50
    if order == 'water':
        return quantity * 1.00
    if order == 'coke':
        return quantity * 1.40
    if order == 'snacks':
        return quantity * 2.00

current_order = input()
current_quantity = int(input())
bill = foo(current_order, current_quantity)

print(f'{bill:.2f}')
