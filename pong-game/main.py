import math
import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from field_decorator import Field_decorator

LEFT_MARGIN = -330
RIGHT_MARGIN = 330
TOP_MARGIN = 210
BOTTOM_MARGIN = -210
LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

field_decorator = Field_decorator()
left_paddle = Paddle(LEFT_PADDLE_POSITION)
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
ball = Ball()

def round_close_to_zero(number):
    tmp = abs(number)
    return math.floor(tmp) if number >= 0 else - math.floor(tmp)


field_decorator.draw_border()

screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "o")
screen.onkey(right_paddle.down, "l")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    ball_x = round_close_to_zero(ball.xcor())
    ball_y = round_close_to_zero(ball.ycor())

    if ball_x > RIGHT_MARGIN or ball_x < LEFT_MARGIN:
        ball.reverse_change_xcor()
    
    if ball_y > TOP_MARGIN or ball_y < BOTTOM_MARGIN:
        ball.reverse_change_ycor()
    
screen.exitonclick()