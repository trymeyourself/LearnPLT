from tkinter import *


def editmenulist(self):
    editmenu=Menu(self, tearoff=0)
    self.add_cascade(label="Edit", menu=editmenu)
    editmenu.add_command(label="Undo", underline=0, accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo", underline=0, accelerator="Ctrl+Y")
    editmenu.add_separator()
    editmenu.add_command(label="Cut", underline=2, accelerator="Ctrl+X")
    editmenu.add_command(label="Copy", underline=2, accelerator="Ctrl+C")
    editmenu.add_command(label="Paste", underline=0, accelerator="Ctrl+V")
    editmenu.add_separator()
    editmenu.add_command(label="Find", underline=0, accelerator="Ctrl+F")
    editmenu.add_command(label="Replace", underline=0, accelerator="Ctrl+H")