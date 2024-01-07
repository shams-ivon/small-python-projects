from tkinter import *

FONT = ("Courier", 15)

window = Tk()
window.title("Mile/KM Converter")
window.minsize(width=400, height=200)
window.config(padx=10, pady=10)

kms = "0"

def miles_to_kms_coverter():
    global kms
    miles = int(input_miles.get())
    kms = miles * 1.609
    km_output.config(text=f"{kms}")

is_equal_to_label_1 = Label(text="Is Equal to :", font=FONT)
is_equal_to_label_1.config(padx=10, pady=10)
is_equal_to_label_1.grid(row=3, column=2)

input_miles = Entry(width=10)
input_miles.grid(row=2, column=3)

miles_label_1 = Label(text="Miles", font=FONT)
miles_label_1.config(padx=10, pady=10)
miles_label_1.grid(row=2, column=4)

km_label_1 = Label(text="KMs", font=FONT)
km_label_1.config(padx=10, pady=10)
km_label_1.grid(row=3, column=4)

km_output = Label(text=f"{kms}", font=FONT)
km_output.config(pady=10)
km_output.grid(row=3, column=3)

miles_to_kms_button = Button(text="convert", command=miles_to_kms_coverter)
miles_to_kms_button.grid(row=4, column=3)

window.mainloop()