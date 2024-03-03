from tkinter import *
def helpmenulist(self):
    helpmenu=Menu(self, tearoff=0)
    self.add_cascade(label="Help", underline=0, menu=helpmenu)

    helpmenu.add_command(label="Welcome", underline=0)
    helpmenu.add_command(label="Documentation", underline=0)
    helpmenu.add_separator()
    helpmenu.add_command(label="Show Release Notes", underline=0)
    helpmenu.add_command(label="Tips and Tricks", underline=0)
    helpmenu.add_separator()
    helpmenu.add_command(label="View License", underline=0)
    helpmenu.add_command(label="Privacy Statement", underline=0)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", underline=0)