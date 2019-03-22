# To Do List v1 simple part 3
# Create textbox

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
        self.task_create = Text(self)                               # Create a text box called task_create
        self.task_create.config(height=3, bg="white", fg="black")   # Format the task_create text box 
        
        # Displaying text box
        self.task_create.pack(side=BOTTOM, fill = X)                # Display task_create in the window
        self.task_create.focus_set()                                # Make task_create the default input



# ---- MAIN PROGRAM----
todo = Window()
todo.mainloop()