from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side = BOTTOM)

button1 = Button(newframe, text="Click here", fg="Magenta")
button2 = Button(newframe, text="Click here", fg="blue")
button1.pack()
button2.pack()





root.mainloop()