from __future__ import print_function
from tkinter import *
from PIL import Image, ImageTk
import random

class App(Frame):

    ships = ["Arleigh Burke Class Destroyer (DDG-51)", "Zumwalt Class Destroyer (DDG-1000)", "Cruiser (CG)", "Littoral Combat Ship (LCS)", "Dock Landing SHIP (LSD)", "Landing Helicopter Assault (LHA)", "Landing Helicopter Dock (LHD)", "Aircraft Carrier (CVN)", "Amphibious Command Ship (LCC)", "Amphibious Transport Dock (LPD)", "Landing Craft Air Cushion (LCAC)", "Mine Counter Measures (MCM)", "Patrol Craft (PC)", "Submarine Tender (AS)"]
    subs = ["Guided Missile Submarine (SSGN)", "Ballistic Missile Submarine (SSBN)", "Fast Attack Submarine (SSN)"]
    fixed = ["C-2 Greyhound", "C-130 Hercules", "E-2C Hawkeye", "E-2D Hawkeye", "E-6B Mercury", "EA-6B Prowler", "EA-18G Growler", "EP-3E Aries", "F/A-18C", "F/A-18D", "F/A-18E", "F/A-18F", "P-8 Poseidon", "P-3 Orion", "T-6B Texan", "T-45 Goshawk", "F-35B Lightning", "F-35C Lightning", "MV-22 Osprey"]
    rotary = ["CH-53 Sea Stallion", "MH-53 Sea Dragon", "MH-60S Seahawk", "MH-60R Seahawk", "TH-57 Sea Ranger", "MV-22 Osprey"]
    unmanned = ["MQ-8 Fire Scout", "MQ-8C Fire Scout", "MQ-4C Triton", "X-47B"]
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
            
            rand = randrange(0, 5)
            length = len(platforms[rand])
            rand2 = randrange(0, length-1)
            rand3 = randrange(0, 10)

            full_name = "images/" + platforms[rand][rand2] + "/" + rand3

            image = Image.open(full_name)
            photo = ImageTk.PhotoImage(image)

            w = Label(self, image=photo)
            w.photo = photo
            w.pack()

            createOptionButtons(self)

            self.button = Button(self, text="SUBMIT", command=self.submit)
            self.button.pack(side=LEFT)


    def submit(self):
        print ("submit")

    def leader(self):
        print ("leaderboard")

    def createOptionButtons(self):

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()

        ray = []
        v5 = randrange(0, length-1)
        text = platforms[rand][v5]
        ray[0] = text

        v6 = randrange(0, length-1)
        while(v6 == v5):
            v6 = randrange(0, length-1)
        text = platforms[rand][v6]
        ray[1] = text

        v7 = randrange(0, length-1)
        while(v7 == v5 || v7 == v6)
            v7 = randrange(0, length-1)
        text = platforms[rand][v7]
        ray[2] = text

        ray[3] = platforms[rand][rand2]

        v8 = randrange(0,3)
        option_text = ray[v8]
        self.option = Radiobutton(self, text=option_text, variable=v1, value=1).pack(anchor=W)

        v9 = randrange(0,3)
        while(v9 == v8)
            v9 = randrange(0,3)
        option_text = ray[v9]
        self.option2 = Radiobutton(self, text=option_text, variable=v2, value=2).pack(anchor=W)

        v10 = randrange(0,3)
        while(v10 == v8 || v10 == v9)
            v10 = randrange(0,3)
        option_text = ray[v10]
        self.option3 = Radiobutton(self, text=option_text, variable=v3, value=3).pack(anchor=W)

        v11 = randrange(0,3)
        while(v11 == v8 || v11 == v9 || v11 == v10)
            v11 = randrange(0,3)
        option_text = ray[v11]
        self.option4 = Radiobutton(self, text=option_text, variable=v4, value=4).pack(anchor=W)


root = Tk()

app = App(root)

root.mainloop()