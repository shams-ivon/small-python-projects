from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARK_GREEN = "#028a0f"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_TEXT_FONT = (FONT_NAME, 50, "bold")
BUTTON_TEXT_FONT = (FONT_NAME, 15)
TIMER_FONT = (FONT_NAME, 35, "bold")
CHECKMARK_FONT = (FONT_NAME, 25, "bold")
TIME_LAPS = 200

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

reps = 1

def start_timer():

    if reps == 0:
        pass

    elif reps % 2 == 1:
        label.config(text="Working Time", fg=GREEN)
        countdown(WORK_MIN)
    
    elif reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN)

    else:
        label.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(current_time):
    global reps
    global checkmarks_string

    current_minute = math.floor(current_time / 60)
    current_second = current_time % 60

    if current_minute < 10:
        current_minute = f"0{current_minute}"

    if current_second < 10:
        current_second = f"0{current_second}"

    canvas.itemconfig(timer_text, text=f"{current_minute}:{current_second}")

    if current_time == 0:

        if reps % 2 == 0:
            checkmarks_string += checkmark
            checkmarks_display.config(text=checkmarks_string)

        reps += 1
        window.after(TIME_LAPS, start_timer)
    
    if current_time > 0:
        window.after(TIME_LAPS, countdown, current_time - 1)

# ---------------------------- UI SETUP ------------------------------- #

checkmark = "✓"
checkmarks_string = ""

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=70, pady=70, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=TIMER_FONT)
canvas.grid(row=2, column=2)

label = Label(text="Timer", font=TIMER_TEXT_FONT, bg=YELLOW, fg=GREEN)
label.grid(row=1, column=2)

checkmarks_display = Label(bg=YELLOW, fg=DARK_GREEN, font=CHECKMARK_FONT)
checkmarks_display.grid(row=4, column=2)

start_button = Button(text="Start", font=BUTTON_TEXT_FONT, bg="white", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", font=BUTTON_TEXT_FONT, bg="white", highlightthickness=0)
reset_button.grid(row=3, column=3)

window.mainloop()