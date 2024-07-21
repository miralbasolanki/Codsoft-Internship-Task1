import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Create GUI components
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=40, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT)

        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:", initialvalue=self.tasks[selected_index])
            if new_task:
                self.tasks[selected_index] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()