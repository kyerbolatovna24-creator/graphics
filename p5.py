import tkinter as tk
from tkinter import messagebox

def validate_input(value):
    if value.strip() == "":
        messagebox.showerror("Input Error", "Input cannot be empty")
        return None

    try:
        number = float(value)
        return number
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")
        return None

def calculate_square(number):
    return number * number

def on_button_click():
    user_input = entry.get()
    number = validate_input(user_input)

    if number is not None:
        result = calculate_square(number)
        result_label.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Square Calculator")

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(
    window,
    text="Calculate",
    command=on_button_click
)
calculate_button.pack()

result_label = tk.Label(window, text="Result:")
result_label.pack()

window.mainloop()