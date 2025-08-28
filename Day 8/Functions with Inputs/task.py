def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name} ?")
    print(f"Isn't the weather nice?")

greet("solomon")

def life_in_weeks(age):
    years_left= 90-age
    weeks_left=years_left * 52
    print(f"You have {weeks_left} weeks left")

life_in_weeks(56)