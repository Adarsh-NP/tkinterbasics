from tkinter import *



root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label='File', menu=submenu)

submenu.add_command(label="Project")

submenu.add_separator()

submenu.add_command(label="Save")

newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=newmenu)
newmenu.add_command(label="undo")

root.mainloop()