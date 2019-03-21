from tkinter import *

class Todo(Tk):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.title("To-Do App v1")
        self.geometry("300x400")

        todo1 = Label(self, text="--- Add Items Here ---")     
        todo1.config(bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        self.task_create = Text(self, height=3, bg="white", fg="black")
        
        self.task_create.pack(side=BOTTOM, fill=X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)

        self.colour_schemes = [("lightgrey", "black"), ("grey","white")]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,END).strip()

        if len(task_text) > 0:
            new_task = Label(self, text=task_text, pady=10)

            task_style_choice = len(self.tasks)%2

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.config(bg=my_scheme_choice[0])
            new_task.config(fg=my_scheme_choice[1])

            new_task.pack(side=TOP, fill=X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, END)

todo = Todo()
todo.mainloop()