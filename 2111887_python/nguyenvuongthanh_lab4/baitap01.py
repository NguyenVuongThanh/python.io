from tkinter import Tk, BOTH, Frame
from tkinter.ttk import Style, Button

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        btn = Button( text="This is Button widget", bg="black", font=("Helvetica", 16))
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)


root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()