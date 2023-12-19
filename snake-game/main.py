import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

LEFT_MARGIN = -260
RIGHT_MARGIN = 260
TOP_MARGIN = 240
BOTTOM_MARGIN = -240

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        scoreboard.update_score()

    if snake.head.xcor() < LEFT_MARGIN or snake.head.xcor() > RIGHT_MARGIN:
        game_is_on = False
    elif snake.head.ycor() < BOTTOM_MARGIN or snake.head.ycor() > TOP_MARGIN:
        game_is_on = False
    
screen.exitonclick()