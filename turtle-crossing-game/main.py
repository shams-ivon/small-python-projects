import time
from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard
from field_decorator import Field_decorator

TIMING = 0.1
SAFE_DISTANCE = 20

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

field_decorator = Field_decorator()
player = Player()
car_manager = Car_manager()

field_decorator.draw_border()
screen.onkey(player.move_forward, "Up")

game_is_on = True
counter = 0

for _ in range(50):
    car_manager.one_move()

while game_is_on:
    time.sleep(TIMING)
    screen.update()
    
    if counter % 3 == 0:
        car_manager.one_move()

    for car in car_manager.cars:
        if car.distance(player) < SAFE_DISTANCE:
            game_is_on = False

    counter += 1

screen.exitonclick()
