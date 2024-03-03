from tkinter import *

def selectmenulist(self):
    selectmenu=Menu(self, tearoff=0)
    self.add_cascade(label="Selection", menu=selectmenu,underline=0)
    selectmenu.add_command(label="Select All", underline=0, accelerator="Ctrl+A")
    selectmenu.add_command(label="Shrink Selection", underline=0, accelerator="Alt+Shift+Left Arrow")
    selectmenu.add_command(label="Expand Selection", underline=0, accelerator="Alt+Shift+Right Arrow")
