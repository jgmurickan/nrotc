from __future__ import print_function
from tkinter import *
from PIL import Image, ImageTk
import random

class App(Frame):

    ships = ["ddg", "cg", "lcs", "lsd", "lha", "lhd", "cvn", "lcc", "lpd", "lcac", "mcm", "pc", "as"]
    subs = ["ssgn", "ssbn", "ssn"]
    fixed = ["c2", "c130", "e2c", "e2d", "e6b", "ea6b", "ea18g", "ep3e", "f18c", "f18d", "f18e", "f18f", "p8", "p3", "t6", "t39", "t45", "f35b", "f35c", "mv-22"]
    rotary = ["ch53", "mh53", "mh60s", "mh60r", "th57", "mv-22"]
    unmanned = ["mq8", "mq4c", "x47"]
    platforms = [ships, subs, fixed, rotary, unmanned]

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

        while(count <= 30):
            randImage = chooseImage();

            image = Image.open(randImage)
            photo = ImageTk.PhotoImage(image)

            w = Label(self, image=photo)
            w.photo = photo
            w.pack()

        v = IntVar()

        self.option = Radiobutton(self, text="Cruiser", variable=v, value=1).pack(anchor=W)
        self.option2 = Radiobutton(self, text="Destroyer", variable=v, value=2).pack(anchor=W)

        self.button = Button(self, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)

    def chooseImage(self):
        rand = randrange()

    def submit(self):
        print ("submit")

    def leader(self):
        print ("leaderboard")

root = Tk()

app = App(root)

root.mainloop()