from turtle import Turtle, Screen
import random

prompt_text = "Which turtle will win the race?: Enter his name: "

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet_turtle = screen.textinput(title="Make your bet!", prompt=prompt_text)

tmnt_name_list = ["leo", "raph", "donny", "mikey"]
tmnt_color_list = [(30, 144, 255), "red", (148, 0, 211), "orange"]
tmnt_y_axis_position_list = [45, 15, -15, -45]
tmnt_object_list = []

for index in range(4):
    current_turtle = Turtle()
    current_turtle.shape("turtle")
    current_turtle.color(tmnt_color_list[index])
    current_turtle.penup()
    current_turtle.goto(x=-200, y=tmnt_y_axis_position_list[index])
    current_turtle.speed(1)
    tmnt_object_list.append(current_turtle)

end_line = Turtle()

end_line.hideturtle()
end_line.penup()

end_line.goto(x=200, y=100)
end_line.pendown()
end_line.goto(x=200, y=-100)

winner_turtle = "leo"

while True:
    index = random.randint(0, 3)
    current_turtle = tmnt_object_list[index]
    current_turtle.forward(10)

    if current_turtle.pos()[0] == 200:
        winner_turtle = tmnt_name_list[index]
        break

if user_bet_turtle == winner_turtle:
    print(f"You win. The winner is {winner_turtle}")
else:
    print(f"You lose. The winner is {winner_turtle}")

screen.exitonclick()