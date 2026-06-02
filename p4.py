import tkinter as tk
from tkinter import messagebox
def save_data():
    name = entry_name.get()
    age = entry_age.get()
    course = course_var.get()
    if name == "" or age == "" or course == "":
        messagebox.showerror("Error", "All fields are required!")
        return
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number!")
        return
    try:
        file = open("students.txt", "a")  # append mode
        file.write(f"{name},{age},{course}\n")
        file.close()

        messagebox.showinfo("Success", "Record saved!")
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "File could not be written!")
def show_records():
    try:
        file = open("students.txt", "r")
        data = file.read()
        file.close()
        if data == "":
            label_output.config(text="No records found.")
        else:
            label_output.config(text=data)
    except:
        label_output.config(text="No file found.")
root = tk.Tk()
root.title("Student Record System")
root.geometry("400x400")
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()
tk.Label(root, text="Course").pack()
course_var = tk.StringVar()
course_var.set("IT")
dropdown = tk.OptionMenu(root, course_var, "IT", "Business", "Engineering", "Design")
dropdown.pack()
tk.Button(root, text="Save", command=save_data).pack(pady=5)
tk.Button(root, text="Show Records", command=show_records).pack(pady=5)
label_output = tk.Label(root, text="", justify="left")
label_output.pack(pady=10)

root.mainloop()