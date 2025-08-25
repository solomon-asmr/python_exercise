print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("How old are you? "))
    payment=0
    if age <= 12:
        payment = 5
    elif age<=18 & age>12:
        payment=7
    else:
        payment=12
    print(f"You should pay {payment}$")
else:
    print("Sorry you have to grow taller before you can ride.")


# BMI Calculator
print("wellcome to BMI calculator")
weight= int(input("please insert your weight: "))
height = int(input("please insert your height: "))
BMI = weight/(height ** 2)
if BMI<18.5:
    print("underweight")
elif BMI<25 & BMI>=18.5:
    print("normal weight")
else: print("overweight")