import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(root, text="My Tasks", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, font=("Helvetica", 12), width=25)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind('<Return>', self.add_task)

        self.add_button = tk.Button(self.input_frame, text="Add", font=("Helvetica", 10, "bold"), 
                                    bg="#4caf50", fg="white", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Listbox with Scrollbar
        self.list_frame = tk.Frame(root, bg="#f0f0f0")
        self.list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_listbox = tk.Listbox(self.list_frame, font=("Helvetica", 12), width=40, height=10,
                                        yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE, 
                                        bg="white", bd=0, highlightthickness=0, activestyle="none")
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        self.scrollbar.config(command=self.tasks_listbox.yview)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=("Helvetica", 11), 
                                       bg="#f44336", fg="white", width=12, command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.mark_button = tk.Button(self.button_frame, text="Mark Done", font=("Helvetica", 11), 
                                     bg="#2196f3", fg="white", width=12, command=self.mark_complete)
        self.mark_button.pack(side=tk.LEFT, padx=10)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task.strip():
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task_text = self.tasks_listbox.get(selected_task_index)
            
            # Simple toggle logic for visual marking
            if task_text.startswith("✔ "):
                 # Unmark
                 new_text = task_text[2:]
                 self.tasks_listbox.itemconfig(selected_task_index, {'fg': 'black'})
            else:
                # Mark
                new_text = "✔ " + task_text
                self.tasks_listbox.itemconfig(selected_task_index, {'fg': 'gray'})

            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, new_text)
            self.tasks_listbox.selection_set(selected_task_index)
            
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
