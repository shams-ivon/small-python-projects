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

x = 0

while x < 15:
    
    x += 1
    snake_size = len(snake_blocks)

    for index in range(snake_size - 1, 0, -1):
        
        next_x = snake_blocks[index - 1].xcor()
        next_y = snake_blocks[index - 1].ycor()
        snake_blocks[index].goto(next_x, next_y)

    snake_blocks[0].forward(20)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()