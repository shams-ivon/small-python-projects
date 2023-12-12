from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_blocks = []
snake_positions = [(0, 0), (-20, 0), (-40, 0)]

for index in range(3):

    block = Turtle("square")
    block.color("white")
    block.penup()
    
    block.goto(snake_positions[index])
    snake_blocks.append(block)

while True:

    for block in snake_blocks:
        block.forward(20)
    
    screen.update()
    time.sleep(0.3)

screen.exitonclick()