from __future__ import print_function
from tkinter import *
from PIL import Image, ImageTk


class App(Frame):

    def __init__(self, parent):

        f = open("results.txt", "w")
        Frame.__init__(self, parent, background="white")
        
        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("UT NROTC Knowledge Game")
        self.pack(fill=BOTH, expand = 1)

        self.start = Button(self, text="Start Quiz", command=self.starter)
        self.start.pack()

        self.lead = Button(self, text="Leaderboard", command=self.leader)
        self.lead.pack()
 
    def starter(self):

        self.start.pack_forget()
        self.lead.pack_forget()

        count = 0

        image = Image.open("images/c_2")
        photo = ImageTk.PhotoImage(image)

        w = Label(self, image=photo)
        w.photo = photo
        w.pack()

        v = IntVar()

        self.option = Radiobutton(self, text="Cruiser", variable=v, value=1).pack(anchor=W)
        self.option2 = Radiobutton(self, text="Destroyer", variable=v, value=2).pack(anchor=W)

        self.button = Button(self, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)


    def submit(self):
        print ("submit")

    def leader(self):
        print ("leaderboard")

root = Tk()

app = App(root)

root.mainloop()