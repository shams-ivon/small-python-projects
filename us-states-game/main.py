import pandas
from turtle import Turtle, Screen

IMAGE = "blank_states_img.gif"
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

collected_states = []

while len(collected_states) < 50:    
    input_state_name = screen.textinput(title=f"{len(collected_states)}/50 states guessed", 
                                        prompt=TEXT_INPUT_PROMPT).title()
    on_list = False

    if input_state_name == "Exit":
        break

    for state in collected_states:

        if state == input_state_name:
            on_list = True
            break
    
    if on_list == True:
        continue

    for index in range(50):
        
        if input_state_name == state_name_list[index]:
            x_cor = state_xcor_list[index]
            y_cor = state_ycor_list[index]
            state_name = state_name_list[index]
            collected_states.append(state_name)
            state_name_writter.goto(x_cor, y_cor)
            state_name_writter.write(state_name)

missing_states = []

for state in state_name_list:

    if state not in collected_states:
        missing_states.append(state)

state_dict = {
    "Missing States": missing_states
}

state_frame = pandas.DataFrame(state_dict)
state_frame.to_csv("missing_states.csv")