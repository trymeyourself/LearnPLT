from tkinter import *

def filemenulist(self):
    filemenu=Menu(self,tearoff=0)
    self.add_cascade(label="File", menu=filemenu, underline=0)
    newsubmenu(filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Open File", underline=0, accelerator="Ctrl+O")
    filemenu.add_command(label="Open Folder",underline=5, accelerator="Ctrl+N")
    filemenu.add_command(label="Open Workspace from file", underline=8)
    filemenu.add_command(label="Open Recent", underline=5)
    filemenu.add_separator()

    filemenu.add_command(label="Add folder to workspace")
    filemenu.add_command(label="save workspace as")
    filemenu.add_command(label="Duplicate Workspace")
    filemenu.add_separator()


    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save As")
    filemenu.add_command(label="Save All")
    filemenu.add_separator()
    sharesubmenu(filemenu)
    filemenu.add_separator()

    filemenu.add_command(label="Auto Save")
    Preferencessubmenu(filemenu)
    filemenu.add_separator()

    filemenu.add_command(label="Revert File")
    filemenu.add_command(label="Close Editor")
    filemenu.add_command(label="Close Folder")
    filemenu.add_separator()
    filemenu.add_command(label="Exit")
   

def Preferencessubmenu(self):
    Prefsubmenulist=Menu(self, tearoff=0)
    self.add_cascade(label="Preferences", menu=Prefsubmenulist)
    Prefsubmenulist.add_command(label="Profiles")
    Prefsubmenulist.add_command(label="Settings")
    Prefsubmenulist.add_command(label="Extenstions")
    Prefsubmenulist.add_command(label="Keyboard Shortcuts")
    Prefsubmenulist.add_command(label="Theme")



def sharesubmenu(self):
    sharesubmenulist=Menu(self, tearoff=0)
    self.add_cascade(label="Share", menu=sharesubmenulist)
    sharesubmenulist.add_command(label="Export Profile")
    sharesubmenulist.add_command(label="Import Profile")


def newsubmenu(self):
    newsubmenulist=Menu(self, tearoff=0)
    self.add_cascade(label="New", menu=newsubmenulist, underline=0)
    newsubmenulist.add_command(label="New Text File", underline=0, accelerator="Ctrl+N")
    newsubmenulist.add_command(label="New File",accelerator="Alt+Ctrl+N")
    newsubmenulist.add_command(label="New Window", underline=4,accelerator="Shift+Ctrl+N")


