from turtle import Screen
from paddle import Paddle
from field_decorator import Field_decorator

LEFT_MARGIN = -370
RIGHT_MARGIN = 370
TOP_MARGIN = 250
BOTTOM_MARGIN = -250
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

field_decorator.draw_border()

game_is_on = True


screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "o")
screen.onkey(right_paddle.down, "l")

while game_is_on:
    screen.update()
    
screen.exitonclick()