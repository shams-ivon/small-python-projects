from turtle import Screen
from snake import Snake

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

x = 0

while x < 15:
    
    x += 1

    screen.update()
    time.sleep(0.1)

    snake.move()
    
screen.exitonclick()