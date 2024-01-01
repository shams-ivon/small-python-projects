import time
from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard
from field_decorator import Field_decorator

TIMING = 0.5

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

for _ in range(50):
    car_manager.one_move()

while game_is_on:
    time.sleep(TIMING)
    screen.update()

    car_manager.one_move()