from turtle import Turtle, Screen
import random

prompt_text = "Which turtle will win the race?: Enter his name: "

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet_turtle = screen.textinput(title="Make your bet!", prompt=prompt_text)

leo = Turtle()
raph = Turtle()
donny = Turtle()
mikey = Turtle()
end_line = Turtle()

end_line.hideturtle()

leo.shape("turtle")
raph.shape("turtle")
mikey.shape("turtle")
donny.shape("turtle")

leo.color((30, 144, 255))
raph.color("red")
donny.color((148, 0, 211))
mikey.color("orange")

leo.penup()
raph.penup()
donny.penup()
mikey.penup()
end_line.penup()

leo.goto(x=-200, y=45)
raph.goto(x=-200, y=15)
donny.goto(x=-200, y=-15)
mikey.goto(x=-200, y=-45)

leo.speed(1)
raph.speed(1)
donny.speed(1)
mikey.speed(1)

end_line.goto(x=200, y=100)
end_line.pendown()
end_line.goto(x=200, y=-100)

winner_turtle = "leo"

while True:
    
    number = random.randint(1, 4)
    
    if number == 1:
        leo.forward(10)
    elif number == 2:
        raph.forward(10)
    elif number == 3:
        donny.forward(10)
    else:
        mikey.forward(10)

    leo_pos = leo.pos()
    raph_pos = raph.pos()
    donny_pos = donny.pos()
    mikey_pos = mikey.pos()

    if leo_pos[0] == 200:
        winner_turtle = "leo"
        break
    elif raph_pos[0] == 200:
        winner_turtle = "raph"
        break
    elif donny_pos[0] == 200:
        winner_turtle = "donny"
        break
    elif mikey_pos[0] == 200:
        winner_turtle = "mikey"
        break

if user_bet_turtle == winner_turtle:
    print(f"You win. The winner is {winner_turtle}")
else:
    print(f"You lose. The winner is {winner_turtle}")

screen.exitonclick()