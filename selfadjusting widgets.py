from tkinter import *

root = Tk()
Label1 = Label(root, text = "Hello there!", bg='blue', fg="White")
Label2 = Label(root, text = "Hello there!", bg='blue', fg="White")



Label1.pack(fill = X)
Label2.pack(side = LEFT, fill=Y)
root.mainloop()