import math
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from field_decorator import Field_decorator

LEFT_MARGIN = -260
RIGHT_MARGIN = 260
TOP_MARGIN = 240
BOTTOM_MARGIN = -240

def round_close_to_zero(number):
    tmp = abs(number)
    return math.floor(tmp) if number >= 0 else - math.floor(tmp)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
field_decorator = Field_decorator()

field_decorator.draw_border()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 17:
        food.new_food_appears()
        snake.extend_snake()
        scoreboard.update_score()

    head_x = round_close_to_zero(snake.head.xcor())
    head_y = round_close_to_zero(snake.head.ycor())

    if head_x < LEFT_MARGIN or head_x > RIGHT_MARGIN:
        scoreboard.reset_score()
        snake.reset()
        continue
        
    elif head_y < BOTTOM_MARGIN or head_y > TOP_MARGIN:
        scoreboard.reset_score()
        snake.reset()
        continue
        
    for block in snake.snake_blocks[1:]:
        
        if snake.head.distance(block) < 10:
            scoreboard.reset_score()
            snake.reset()
            break
    
screen.exitonclick()