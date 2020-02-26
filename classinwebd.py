from tkinter import *

root = Tk()


class Buttons:

    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.button = Button(frame, text="Click here", command=self.printmsg)
        self.button.pack()

        self.quit = Button(frame, text="Exit", command=frame.quit)
        self.quit.pack(side=LEFT)

    def printmsg(self):
        print("button clicked")


# root = Tk()

b = Buttons(root)

root.mainloop()
