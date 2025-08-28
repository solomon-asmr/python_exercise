# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location} ?")

# name=input("What is your name ?")
# Location = input("Where do you live ?")
# greet_with(input("What is your name ?"), input("Where do you live ?"))


def calculate_love_score(name1, name2):
    names=""
    name1.lower()
    name2.lower()
    true="true"
    love="love"
    names+=name1
    names+=name2
    print(names)
    sum1=0
    sum2=0
    for letter in names:
        for tri in true:
            if tri==letter:
                sum1+=1
    for lett in names:
        for trii in love:
            if trii==lett:
                sum2+=1
    print(str(sum1)+""+str(sum2))


calculate_love_score("angela yu", "jack bauer")