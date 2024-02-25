from tkinter import *
from menus.filemenu import *
from menus.editmenu import *
from menus.gomenu import *
from menus.selectmenu import *
from menus.runmenu import *
from menus.viewmenu import *
from menus.terminalmenu import *
from menus.helpmenu import *

def mainmenu(self):

    menulist=Menu(self)
    filemenulist(menulist)
    editmenulist(menulist)
    selectmenulist(menulist)
    viewmenulist(menulist)
    gomenulist(menulist)
    runmenulist(menulist)
    terminalmenulist(menulist)
    helpmenulist(menulist)
    self.config(menu=menulist)
    

    





