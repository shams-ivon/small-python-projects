import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x = 0

while x < 200:
    
    x += 1

    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) <= 14:
        
        food.new_food_appears()
    
screen.exitonclick()