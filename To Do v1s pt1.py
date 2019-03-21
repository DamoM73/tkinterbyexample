# To Do List v1 simple part 1
# Create a Window

from tkinter import *

class Window(Tk):                       # creates an object of window type (TK)
    def __init__(self):                 # initialising function which is run when the object is created
        super().__init__()              # call the initialisation function of parent class (TK)

        # Window details
        self.title("To-Do App v1")      # text of the title bar
        self.geometry("300x400")        # size of the window


# ---- MAIN PROGRAM----
todo = Window()                         # create a tkinter window object and store as todo
todo.mainloop()                         # run the todo window (tkinter method)