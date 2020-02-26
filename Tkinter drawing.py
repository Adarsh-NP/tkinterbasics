from tkinter import *

root = Tk()

canvas1 = Canvas(root, width=200, height=100)
canvas1.pack()

newline = canvas1.create_line(0,0, 50,100)
otherline = canvas1.create_line(0, 10, 100, 100, fill = "green")


root.mainloop()