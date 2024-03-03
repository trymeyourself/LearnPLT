from tkinter import *

def viewmenulist(self):
    viewmenu=Menu(self, tearoff=0)
    self.add_cascade(label="View", underline=0,menu=viewmenu)
    viewmenu.add_command(label="Appearance", underline=0)
    viewmenu.add_command(label="Editor Layout", underline=0)
    viewmenu.add_separator()
    viewmenu.add_command(label="Search", underline=0, accelerator="Ctrl+Shift+F")
    viewmenu.add_command(label="Search", underline=0, accelerator="Ctrl+Shift+F")
    viewmenu.add_command(label="Word Wrap", underline=0, accelerator="Alt+Z")