from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("title", "THIS IS AWESOME")

response = tkinter.messagebox.askquestion("Ques1", "Do you like coffee?")

if response == 'yes':
    print("Here's one for you")


root.mainloop()