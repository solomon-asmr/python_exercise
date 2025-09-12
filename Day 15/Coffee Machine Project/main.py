MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0
#TODO: 1. use while loop to let customers choose their order either espresso/latte/cappuccino:
#TODO: 1.1: use if clause to decide what to do next
#TODO: 2. when the admin inserts secrete word "off" to the prompt the system will stop working
#TODO: 3. when the user enters "report" to the prompt report will be generated that shows the current resource  values.
    # water: 100ml
    # milk: 50ml
    # coffee: 76g
    # money: $2.5
# TODO: 4. check resources sufficient when the user chooses a drink, the program should check if there are enough resources
# TODO: 5. process coins if there are sufficient resources to make the drink selected, then the program should prompt
#             the user to insert coins
while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("sorry there is not enough water")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("sorry there is not enough coffee")
        else:
            print("please insert coins.")
            quarters=int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            monex = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if MENU["espresso"]["cost"]>monex:
                print("Sorray that's not enough money. money refunded")
            else:
                resources["water"]-=MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                if MENU["espresso"]["cost"] < monex:
                    print(f"Here is ${monex-MENU['espresso']['cost']} dollars in change.")
                print("Here is your espresso. Enjoy!")
                money+=MENU["espresso"]["cost"]

    elif choose == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("sorry there is not enough water")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("sorry there is not enough milk")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("sorry there is not enough coffee")
        else:
            print("please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            monex=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
            if MENU["latte"]["cost"]>monex:
                print("Sorray that's not enough money. money refunded")
            else:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                if MENU["latte"]["cost"] < monex:
                    print(f"Here is ${monex - MENU['latte']['cost']} dollars in change.")
                print("Here is your latte. Enjoy!")
                money += MENU["latte"]["cost"]

    elif choose == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("sorry there is not enough water")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("sorry there is not enough milk")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("sorry there is not enough coffee")
        else:
            print("please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            monex = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if MENU["cappuccino"]["cost"]>monex:
                print("Sorray that's not enough money. money refunded")
            else:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                if MENU["cappuccino"]["cost"] < monex:
                    print(f"Here is ${monex - MENU['cappuccino']['cost']} dollars in change.")
                print("Here is your cappuccino. Enjoy!")
                money += MENU["cappuccino"]["cost"]

    elif choose == "report":
        rep=f"water: {resources['water']} \n milk: {resources['milk']}\n coffe: {resources['coffee']}\n money: ${money}"
        print(rep)
    elif choose == "off":
        break
    else:
        print("please insert the correct prompt")

