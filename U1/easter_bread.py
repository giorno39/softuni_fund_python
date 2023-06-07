budget = float(input())
price_of_flour = float(input())
price_of_eggs = 0.75 * price_of_flour
price_of_milk_liter = (0.25 * price_of_flour) + price_of_flour
price_of_milk = price_of_milk_liter / 4
price_for_one_bread = price_of_eggs + price_of_flour + price_of_milk

number_of_breads = 0
eggs = 0

while budget > price_for_one_bread:
    eggs += 3
    number_of_breads +=1
    budget -= price_for_one_bread
    if number_of_breads % 3 == 0:
        eggs -= (number_of_breads - 2)

print(f"You made {number_of_breads} loaves of Easter bread! "
      f"Now you have {eggs} eggs and {budget:.2f}BGN left.")
