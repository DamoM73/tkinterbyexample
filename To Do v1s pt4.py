# To Do List v1 simple part 4
# Make text_box and add task to list

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
        self.bind("<Return>", self.add_task)                        # When return is pressed, add_task() is called                           

    def add_task(self, event=None):
        # Retrieve task from text box
        task_text = self.task_create.get(1.0,END).strip()           # Assigns text and removes return at EOL
        
        # Create new task and prepare to dsiplay
        new_task = Label(self, text=task_text, pady=10)             # makes a lable from content of task_text
        new_task.pack(side=TOP, fill=X)                             # prepares label to be displayed
        
        # Add task to tasks list
        self.tasks.append(new_task)                                 # add label to tasks list

        # clear the text box
        self.task_create.delete(1.0, END)                           # Clears task_create box


# ---- MAIN PROGRAM----
todo = Window()
todo.mainloop()