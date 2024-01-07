import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from field_decorator import FieldDecorator

TIMING = 0.1
DIVIDE = 1.5
SAFE_DISTANCE = 20

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

field_decorator = FieldDecorator()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

field_decorator.draw_border()
screen.onkey(player.move_forward, "Up")

game_is_on = True
counter = 0

for _ in range(50):
    car_manager.one_move()

while game_is_on:
    time.sleep(TIMING)
    screen.update()
    
    if counter % 5 == 0:
        car_manager.one_move()

    for car in car_manager.cars:
        
        if car.distance(player) < SAFE_DISTANCE:
            game_is_on = False
        
    if player.is_at_finish_line() == True:
        scoreboard.level_up()
        car_manager.speed_up()
        player.goto_start()
        continue

    counter += 1

screen.exitonclick()
