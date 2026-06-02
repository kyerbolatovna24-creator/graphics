import tkinter as tk
from tkinter import messagebox

def calculate_cube():
    value = entry.get()

    if value == "":
        messagebox.showerror("Error", "Input field is empty!")
        return

    try:
        number = float(value)
        cube = number ** 3
        result_label.config(text=f"Result: {cube}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")


window = tk.Tk()
window.title("Cube Calculator")
window.geometry("300x200")


label = tk.Label(window, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate Cube", command=calculate_cube)
calculate_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

result_label = tk.Label(window, text="Result:")
result_label.pack(pady=10)


window.mainloop()