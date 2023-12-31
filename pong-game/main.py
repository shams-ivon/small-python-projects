import math
import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from field_decorator import Field_decorator

LEFT_MARGIN = -330
RIGHT_MARGIN = 330
TOP_MARGIN = 210
BOTTOM_MARGIN = -210
LEFT_TOUCH = -320
RIGHT_TOUCH = 320
LEFT_MISS = -340
RIGHT_MISS = 340
PADDLE_CENTRE_TO_BALL_CENTRE = 45
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
scoreboard = Scoreboard()

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
    time.sleep(0.15)
    ball.move()

    ball_x = round_close_to_zero(ball.xcor())
    ball_y = round_close_to_zero(ball.ycor())

    if ball_x < LEFT_MISS:
        ball.goto(0, 0)
        ball.reverse_change_xcor()
        scoreboard.increase_right_score()
        continue
    
    if ball_x > RIGHT_MISS:
        ball.goto(0, 0)
        ball.reverse_change_xcor()
        scoreboard.increase_left_score()
        continue

    if ball_y > TOP_MARGIN or ball_y < BOTTOM_MARGIN:
        ball.reverse_change_ycor()
    
    if left_paddle.distance(ball) <= PADDLE_CENTRE_TO_BALL_CENTRE and ball_x <= LEFT_TOUCH:
        ball.reverse_change_xcor()

    if right_paddle.distance(ball) <= PADDLE_CENTRE_TO_BALL_CENTRE and ball_x >= RIGHT_TOUCH:
        ball.reverse_change_xcor()

screen.exitonclick()