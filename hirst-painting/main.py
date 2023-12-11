from extracted_colors import color_tuple_list
from turtle import Turtle, Screen
import random

upto = len(color_tuple_list) - 1

screen = Screen()
screen.colormode(255)

arrow_turtle = Turtle()
arrow_turtle.width(10)
arrow_turtle.penup()
arrow_turtle.hideturtle()
arrow_turtle.speed(0)

arrow_turtle.left(225)
arrow_turtle.forward(200)
arrow_turtle.right(225)

for i in range(10):
    
    color = color_tuple_list[random.randint(0, upto)]
    arrow_turtle.color(color)
    arrow_turtle.dot()

    for j in range(9):

        arrow_turtle.forward(40)
        color = color_tuple_list[random.randint(0, upto)]
        arrow_turtle.color(color)
        arrow_turtle.dot()

    arrow_turtle.left(90)
    arrow_turtle.forward(40)
    arrow_turtle.left(90)
    arrow_turtle.forward(9 * 40)
    arrow_turtle.right(180)
        
screen.exitonclick()