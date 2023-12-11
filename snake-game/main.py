from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_blocks = []
snake_positions = [0, -20, -40]

for index in range(3):

    block = Turtle("square")
    block.color("white")
    block.penup()
    block.speed(0)
    block.goto(x=snake_positions[index], y=0)
    snake_blocks.append(block)

screen.exitonclick()