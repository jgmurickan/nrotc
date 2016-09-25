from __future__ import print_function
from Tkinter import *
from PIL import Image, ImageTk


class App:

    frame = Frame()

    def __init__(self, master):

        f = open("results.txt", "w")

        
        frame = Frame(master)
        frame.pack()

        self.start = Button(frame, text="Start Quiz", command=self.starter)
        self.start.pack()
        self.lead = Button(frame, text="Leaderboard", command=self.leader)
        self.lead.pack()


    def starter(self):

        count = 0

        image = Image.open("images/c_2")
        photo = ImageTk.PhotoImage(image)

        w = Label(frame, image=photo)
        w.photo = photo
        w.pack()

        v = IntVar()

        self.option = Radiobutton(frame, text="Cruiser", variable=v, value=1).pack(anchor=W)
        self.option2 = Radiobutton(frame, text="Destroyer", variable=v, value=2).pack(anchor=W)

        self.button = Button(frame, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)

    def submit(self):
        print ("submit")

    def leader(self):
        print ("leaderboard")

root = Tk()

app = App(root)

root.mainloop()