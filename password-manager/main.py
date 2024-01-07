from tkinter import *

LABEL_FONT = ("Courier", 15)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid(row=1, column=2)

website_label = Label(text="Website :", font=LABEL_FONT)
website_label.grid(row=2, column=1)

email_label = Label(text="Email/Username :", font=LABEL_FONT)
email_label.grid(row=3, column=1)

password_label = Label(text="Password :", font=LABEL_FONT)
password_label.grid(row=4, column=1)

website_entry = Entry(width=37)
website_entry.grid(row=2, column=2, columnspan=2)

email_entry = Entry(width=37)
email_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry()
password_entry.grid(row=4, column=2, columnspan=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=35)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()