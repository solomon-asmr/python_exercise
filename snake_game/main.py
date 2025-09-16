# Todo 1: Create snake body with 3 squares
# Todo 2: move the snake
# Todo 3: Create snake food
# Todo 4: Detect collision with the food
# Todo 5: Create a scoreboard
# Todo 6: Detect collision with wall
# Todo 7: Detect collision with the tail
import time
from turtle import Turtle, Screen
from snake import Snake
screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

















screen.exitonclick()