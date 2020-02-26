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

toolbar = Frame(root)
insertbutton = Button(toolbar, text = "Insert files")
insertbutton.pack(side = LEFT, padx=2, pady=3, fill = X)

printbutton = Button(toolbar, text = "print")
printbutton.pack(side = LEFT, padx=2, pady=3, fill = X)

toolbar.pack(side= TOP, fill = X)

status = Label(root, text="this is the status", bd=1, relief=SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill=X)

root.mainloop()