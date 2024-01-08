import json
from tkinter import *
from tkinter import messagebox
import random

LABEL_FONT = ("Courier", 15)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = []

    password_size = random.randint(8, 12)
    total_letters = random.randint(1, password_size - 3)
    total_numbers = password_size - total_letters

    password_letters = [random.choice(letters) for _ in range(total_letters)]
    password_numbers = [random.choice(numbers) for _ in range(total_numbers)]

    password_list = password_letters + password_numbers
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)

# --------------------------------- SEARCH -------------------------------------- #

def search_password():
    website_name = website_entry.get()

    if len(website_name) == 0:
        messagebox.showinfo(message="Please, insert a website's name.")
        return

    try:
        with open("saved_passwords.json", "r") as file:
            existing_data = json.load(file)
    
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found")
        return
    
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(message="Password isn't saved for this website.")
        return

    try:
        website_data = existing_data[website_name]
    
    except KeyError:
        messagebox.showinfo(message="Password isn't saved for this website.")

    else:
        messagebox.showinfo(message=f"Website: {website_name}\n"
                            f"Email: {website_data['email']}\n"
                            f"Password: {website_data['password']}")
        
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error!", message="Please, don't leave any fields empty!")
        return
    
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    is_ok = messagebox.askokcancel(title=website, message=f"Website: {website}\n"
                                                f"Email: {email}\nPassword: {password}\n"
                                                f"\nAre you sure you want to save the informations?")
    
    if is_ok:

        try:
            with open("saved_passwords.json", "r") as file:
                existing_data = json.load(file)
                existing_data.update(new_data)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("saved_passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            with open("saved_passwords.json", "w") as file:
                json.dump(existing_data, file, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")
        website_entry.focus()

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

website_entry = Entry()
website_entry.focus()
website_entry.grid(row=2, column=2)

email_entry = Entry(width=37)
email_entry.insert(0, "abc@efg.com")
email_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry()
password_entry.grid(row=4, column=2, columnspan=1)

search_button = Button(text="Search Password", width=13, command=search_password)
search_button.grid(row=2, column=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()