print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    choice = input("You can ride the rollercoaster. do you wanna photo y/n: ")
    total_payment=0
    if choice=='y':
        total_payment+=3
    age = int(input("What is your age? "))
    if age <= 12:
        total_payment+=5
    elif age <= 18:
        total_payment+=7
    else:
        total_payment += 12
    print(f"Please pay ${total_payment}.")
else:
    print("Sorry you have to grow taller before you can ride.")
