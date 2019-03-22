# To Do List v1 simple complete
# make a list of To Do items

from tkinter import *

class Todo(Tk):
    def __init__(self):
        super().__init__()

        # Object vairables
        self.tasks = []

        # Window details
        self.title("To-Do App v1")
        self.geometry("300x400")

        # Adding instructions to tasks
        todo1 = Label(self, text="--- Add Items Here ---")     
        todo1.config(bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)

        # Display tasks
        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        # Create text box
        self.task_create = Text(self)
        self.task_create.config(height=3, bg="white", fg="black")
        
        # Displaying text box
        self.task_create.pack(side=BOTTOM, fill=X)
        self.task_create.focus_set()

        # Event handler
        self.bind("<Return>", self.add_task)

        self.colour_schemes = [("lightgrey", "black"), ("grey","white")]

    def add_task(self, event=None):
        # Retieve task from text box
        task_text = self.task_create.get(1.0,END).strip()

        # Create new task and prepare to dsiplay
        new_task = Label(self, text=task_text, pady=10)
        task_style_choice = len(self.tasks) % 2
        my_scheme_choice = self.colour_schemes[task_style_choice]
        new_task.config(bg=my_scheme_choice[0])
        new_task.config(fg=my_scheme_choice[1])
        new_task.pack(side=TOP, fill=X)

        # Add task to task list
        self.tasks.append(new_task)

        # clear the text box
        self.task_create.delete(1.0, END)


# ---- MAIN PROGRAM ----
todo = Todo()
todo.mainloop()