import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from a file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task function
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Mark task as done
def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

# Delete task function
def delete_task():
    try:
        index = task_listbox.curselection()[0]
        del tasks[index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Update Listbox display
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# Initialize app
tasks = load_tasks()

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry widget for adding tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

mark_done_button = tk.Button(root, text="Mark as Done", command=mark_done)
mark_done_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Load and display existing tasks
update_listbox()

# Run app
root.mainloop()
