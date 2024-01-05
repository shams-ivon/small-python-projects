import pandas
from turtle import Turtle, Screen

IMAGE = "blank_states_img.gif"
TEXT_INPUT_TITLE = "Guess The State"
TEXT_INPUT_PROMPT = "Give a state's name..."

state_data = pandas.read_csv("50_states.csv")
state_name_list = state_data["state"].tolist()
state_xcor_list = state_data["x"].tolist()
state_ycor_list = state_data["y"].tolist()

screen = Screen()
turtle = Turtle()
state_name_writter = Turtle()

screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
state_name_writter.hideturtle()
state_name_writter.penup()


while True:    
    input_state_name = screen.textinput(title=TEXT_INPUT_TITLE, prompt=TEXT_INPUT_PROMPT)
    
    for index in range(50):
        
        if input_state_name.lower() == state_name_list[index].lower():
            x_cor = state_xcor_list[index]
            y_cor = state_ycor_list[index]
            state_name = state_name_list[index]
            state_name_writter.goto(x_cor, y_cor)
            state_name_writter.write(state_name)

screen.exitonclick()