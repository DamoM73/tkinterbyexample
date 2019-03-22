# To Do List v1 simple part 4
# Formate the tasks

from tkinter import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        
        # Object variables
        self.tasks = []
        
        # Window details
        self.title("To-Do App v1")
        self.geometry("300x400")

        # Adding instructions to tasks
        todo1 = Label(self, text="--- Add Items Here ---")
        todo1.config(bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)

        # Displaying tasks
        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        # Create text box
        self.task_create = Text(self)
        self.task_create.config(height=3, bg="white", fg="black")
        
        # Displaying text box
        self.task_create.pack(side=BOTTOM, fill = X)
        self.task_create.focus_set()

        # Event handler
        self.bind("<Return>", self.add_task)

        # Colour Scheme
        self.colour_scheme = [("lightgrey", "black"), ("grey","white")]     # A list of colour scheme tupples

    def add_task(self, event=None):
        # Retrieve task from text box
        task_text = self.task_create.get(1.0,END).strip()
        
        # Create new task and prepare to dsiplay
        new_task = Label(self, text=task_text, pady=10)
        task_style_choice = len(self.tasks) % 2                             # Establish which colour scheme to apply
        my_scheme_choice = self.colour_scheme[task_style_choice]           # Choose that scheme from the list
        new_task.config(bg=my_scheme_choice[0])                             # Applies the background colour
        new_task.config(fg=my_scheme_choice[1])                             # Applies teh foreground colour
        new_task.pack(side=TOP, fill=X)
        
        # Add task to tasks list
        self.tasks.append(new_task)

        # clear the text box
        self.task_create.delete(1.0, END)


# ---- MAIN PROGRAM----
todo = Window()
todo.mainloop()