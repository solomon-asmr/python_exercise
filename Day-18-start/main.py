import random
import turtle
from itertools import count
#
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# timmy_the_turtle = turtle.Turtle()
# timmy_the_turtle.shape("turtle")
# degree = 360
# countt=3
# i=0
# while True:
#     if countt<9:
#         degrees=degree/countt
#         for _ in range(countt):
#             timmy_the_turtle.forward(50)
#             timmy_the_turtle.right(degrees)
#
#         timmy_the_turtle.color(colors[i])
#         i+=1
#         countt+=1
#
#     else:
#         break

# your drawing code here



turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim=turtle.Turtle()
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(10)

turtle.done()  # keeps the window open until closed properly
