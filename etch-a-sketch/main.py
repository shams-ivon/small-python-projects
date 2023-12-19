from turtle import Turtle, Screen

screen = Screen()
arrow_turtle = Turtle()

def go_foroward():
    arrow_turtle.forward(20)

def go_backward():
    arrow_turtle.backward(20)

def turn_left():
    arrow_turtle.left(10)

def turn_right():
    arrow_turtle.right(10)

def clear():
    arrow_turtle.clear()
    arrow_turtle.penup()
    arrow_turtle.speed(0)
    arrow_turtle.goto(0, 0)
    arrow_turtle.setheading(0)
    arrow_turtle.pendown()

screen.listen()
screen.onkey(key="w", fun=go_foroward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()