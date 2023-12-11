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

# for index in range(4):
    
#     current_turtle = Turtle()
#     current_turtle.shape("turtle")
#     current_turtle.color(tmnt_color_list[index])
#     current_turtle.penup()
#     current_turtle.goto(x=-200, y=tmnt_y_axis_position_list[index])
#     current_turtle.speed(1)
#     tmnt_object_list.append(current_turtle)

# end_line = Turtle()

# end_line.hideturtle()
# end_line.penup()

# end_line.goto(x=200, y=100)
# end_line.pendown()
# end_line.goto(x=200, y=-100)

# winner_turtle = "leo"

# while True:
    
#     number = random.randint(0, 3)
    
#     if number == 1:
#         leo.forward(10)
#     elif number == 2:
#         raph.forward(10)
#     elif number == 3:
#         donny.forward(10)
#     else:
#         mikey.forward(10)

#     leo_pos = leo.pos()
#     raph_pos = raph.pos()
#     donny_pos = donny.pos()
#     mikey_pos = mikey.pos()

#     if leo_pos[0] == 200:
#         winner_turtle = "leo"
#         break
#     elif raph_pos[0] == 200:
#         winner_turtle = "raph"
#         break
#     elif donny_pos[0] == 200:
#         winner_turtle = "donny"
#         break
#     elif mikey_pos[0] == 200:
#         winner_turtle = "mikey"
#         break

# if user_bet_turtle == winner_turtle:
#     print(f"You win. The winner is {winner_turtle}")
# else:
#     print(f"You lose. The winner is {winner_turtle}")

# screen.exitonclick()