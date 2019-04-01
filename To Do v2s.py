from tkinter import *
import tkinter.messagebox as msg

class Todo(Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Window values
        self.title("To-Do App v2")
        self.geometry("300x400")        

        # Create the canvas for the tasks to be listed
        self.tasks_canvas = Canvas(self)
        self.tasks_frame = Frame(self.tasks_canvas)                     # add a frame to the canvas to contain tasks        
        self.scrollbar = Scrollbar(self.tasks_canvas, \
            orient="vertical", command=self.tasks_canvas.yview)         # add scrollbar to the canvas
        self.tasks_canvas.config(yscrollcommand=self.scrollbar.set)
        
        # Create a frame for the textbox
        self.text_frame = Frame(self)


        

        self.task_create = Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=TOP, fill=BOTH, expand = 1)
        self.scrollbar.pack(side=RIGHT, fill= Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=BOTTOM, fill=X)
        self.text_frame.pack(side=BOTTOM, fill=X)
        self.task_create.focus_set()

        todo1 = Label(self.tasks_frame, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        todo1.bind("<Button-1>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>",self.mouse_scroll)
        self.bind_all("<Button-5>",self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [{"bg": "lightgrey", "fg":"black"},{"bg":"grey", "fg":"white"}]

    def add_task(self, event=None):        
        task_text = self.task_create.get(1.0, END).strip()

        if len(task_text) > 0:
            new_task = Label(self.tasks_frame, text=task_text, pady=10)
            
            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=TOP, fill=X)

            self.tasks.append(new_task)
        
        self.task_create.delete(1.0, END)

    def remove_task(self,event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)
    
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.config(bg=my_scheme_choice["bg"])
        task.config(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.config(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()