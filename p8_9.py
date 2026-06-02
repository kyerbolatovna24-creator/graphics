import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Data Manager")
window.geometry("350x400")

students = []

tk.Label(window, text="Name:").pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

tk.Label(window, text="Age:").pack(pady=5)
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

output_label = tk.Label(window, text="No data yet", justify="left")
output_label.pack(pady=10)


def add_student():
    name = name_entry.get()
    age = age_entry.get()

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number")
        return

    student = f"{name} - {age}"
    students.append(student)

    messagebox.showinfo("Success", "Student added!")

    clear_fields()


def show_students():
    if not students:
        output_label.config(text="No students added")
    else:
        result = "Students List:\n"
        for s in students:
            result += s + "\n"

        output_label.config(text=result)


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


tk.Button(window, text="Add Student",
          command=add_student).pack(pady=5)

tk.Button(window, text="Show All Students",
          command=show_students).pack(pady=5)

tk.Button(window, text="Clear",
          command=clear_fields).pack(pady=5)

window.mainloop()