import random
from turtle import Turtle, Screen

screen=Screen()
is_bet_on=False
screen.setup(width=500, height=400)
colors=["red", "orange", "yellow", "green", "blue", "purple"]
y_position= [-70, -40, -10, 20, 50, 80]
all_turtles=[]

for turtl_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtl_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtl_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

if user_bet:
    is_bet_on=True

while is_bet_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_bet_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()