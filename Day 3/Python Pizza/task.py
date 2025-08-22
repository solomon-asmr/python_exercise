print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0
small_pizza = 15
medium_pizza = 20
LargePizza = 25
pepperoni_small = 2
pepperoni_large_medium = 3
extra_cheese_bill = 1

if size == 'S':
    total_bill += small_pizza
    if pepperoni == 'Y':
        total_bill += pepperoni_small
    if extra_cheese == 'Y':
        total_bill+= extra_cheese_bill
elif size == 'M':
    total_bill += medium_pizza
    if pepperoni == 'Y':
        total_bill += pepperoni_large_medium
    if extra_cheese == 'Y':
        total_bill+= extra_cheese_bill
elif size == 'L':
    total_bill += LargePizza
    if pepperoni == 'Y':
        total_bill += pepperoni_large_medium
    if extra_cheese == 'Y':
        total_bill+= extra_cheese_bill
else: print("you typed the wrong input!")
print(f"Your final bill is: ${total_bill}.")
