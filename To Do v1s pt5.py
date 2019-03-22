# To Do List v1 simple part 2
# Add task to task_list

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

    def add_task(self, event=None):
        # Retrieve task from text box
        task_text = self.task_create.get(1.0,END)
        task_text.strip()

        # add task to task

        # clear the text box
        self.task_create.delete(1.0, END)


# ---- MAIN PROGRAM----
todo = Window()
todo.mainloop()