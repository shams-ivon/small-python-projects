from turtle import Screen
from paddle import Paddle
from field_decorator import Field_decorator

LEFT_MARGIN = -370
RIGHT_MARGIN = 370
TOP_MARGIN = 250
BOTTOM_MARGIN = -250
LEFT_PADDLE_INIT_X = -350
LEFT_PADDLE_INIT_Y = 0
RIGHT_PADDLE_INIT_X = 350
RIGHT_PADDLE_INIT_Y = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# screen.tracer(0)
screen.listen()

field_decorator = Field_decorator()
left_paddle = Paddle(LEFT_PADDLE_INIT_X, LEFT_PADDLE_INIT_Y)
right_paddle = Paddle(RIGHT_PADDLE_INIT_X, RIGHT_PADDLE_INIT_Y)

field_decorator.draw_border()

# screen.update()

screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "o")
screen.onkey(right_paddle.down, "l")

screen.exitonclick()