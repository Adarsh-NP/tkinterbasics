from tkinter import *

def function1():
    print("you clicked the button")

root = Tk()

Label1 = Label(root, text="first name", bg = "red", fg = "White")
Label2 = Label(root, text="last name", bg = "red", fg = "White")

entry1 = Entry(root, bg = "Sky blue")
entry2 = Entry(root, bg = "Sky blue")

button = Button(root, text = "Click here", bg = "Blue", fg= "White", command = function1)

Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
button.grid(row = 3, column = 2)




root.mainloop()