import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Registration")
window.geometry("400x400")

# Name
tk.Label(window, text="Name:").pack(pady=5)
entry_name = tk.Entry(window)
entry_name.pack(pady=5)

# Gender (Radiobutton)
tk.Label(window, text="Gender:").pack(pady=5)

gender = tk.StringVar()
gender.set("Male")

rb1 = tk.Radiobutton(window, text="Male", variable=gender, value="Male")
rb2 = tk.Radiobutton(window, text="Female", variable=gender, value="Female")

rb1.pack()
rb2.pack()

# Country (Dropdown)
tk.Label(window, text="Country:").pack(pady=5)

country = tk.StringVar()
country.set("Kazakhstan")

dropdown = tk.OptionMenu(
    window,
    country,
    "Kazakhstan",
    "Russia",
    "USA",
    "Germany",
    "China"
)
dropdown.pack(pady=5)

# Agree (Checkbox)
agree = tk.IntVar()

checkbox = tk.Checkbutton(
    window,
    text="I agree to the terms",
    variable=agree
)
checkbox.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)


def submit():
    name = entry_name.get()

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if agree.get() == 0:
        messagebox.showerror("Error", "You must agree to the terms")
        return

    result = (
        f"Name: {name}\n"
        f"Gender: {gender.get()}\n"
        f"Country: {country.get()}"
    )

    result_label.config(text=result)
    messagebox.showinfo("Success", "Data submitted!")


btn_submit = tk.Button(window, text="Submit", command=submit)
btn_submit.pack(pady=10)

window.mainloop()