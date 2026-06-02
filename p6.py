import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if name == "":
        messagebox.showerror("Input Error", "Name cannot be empty")
        return

    if not age.isdigit():
        messagebox.showerror("Input Error", "Age must be a number")
        return

    if grade == "":
        messagebox.showerror("Input Error", "Grade cannot be empty")
        return

    result_text = f"Student: {name}\nAge: {age}\nGrade: {grade}"
    label_result.config(text=result_text)

def clear_data():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    label_result.config(text="")

window = tk.Tk()
window.title("Student Information Form")

tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
entry_grade = tk.Entry(window)
entry_grade.grid(row=2, column=1, padx=10, pady=5)

btn_submit = tk.Button(window, text="Submit", command=submit_data)
btn_submit.grid(row=3, column=0, padx=10, pady=10)

btn_clear = tk.Button(window, text="Clear", command=clear_data)
btn_clear.grid(row=3, column=1, padx=10, pady=10)

label_result = tk.Label(window, text="", fg="blue", justify="left")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()