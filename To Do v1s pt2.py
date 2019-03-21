# To Do List v1 simple part 2
# Add instructions

from tkinter import *

class Window(Tk):
    def __init__(self):
        super().__init__()

        # Object variables
        self.tasks = []                                         # create a list to store the tasks
        
        # Window details
        self.title("To-Do App v1")
        self.geometry("300x400")

        # Adding instructions to tasks
        todo1 = Label(self, text="--- Add Items Here ---")      # creates a label and assigns it to todo1
        todo1.config(bg="lightgrey", fg="black", pady=10)       # formats the label in todo1
        self.tasks.append(todo1)                                # adds the label in todo1 to the end of the tasks list

        # Displaying tasks
        for task in self.tasks:                                 # loops through every task in the tasks list
            task.pack(side=TOP, fill=X)                         # write the task to the screen


# ---- MAIN PROGRAM----
todo = Window()
todo.mainloop()