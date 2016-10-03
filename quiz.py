from __future__ import print_function
from tkinter import *
from PIL import Image, ImageTk
import random

ships = ["Arleigh Burke Class Destroyer (DDG-51)", "Zumwalt Class Destroyer (DDG-1000)", "Cruiser (CG)", "Littoral Combat Ship (LCS)", "Dock Landing Ship (LSD)", "Landing Helicopter Assault (LHA)", "Landing Helicopter Dock (LHD)", "Aircraft Carrier (CVN)", "Amphibious Command Ship (LCC)", "Amphibious Transport Dock (LPD)", "Landing Craft Air Cushion (LCAC)", "Mine Counter Measures (MCM)", "Patrol Coastal Ship (PC)", "Submarine Tender (AS)"]
subs = ["Ohio-Class Guided Missile Submarine (SSGN)", "Ohio-Class Ballistic Missile Submarine (SSBN)", "Virginia-Class Fast Attack Submarine (SSN)", "Los Angeles-Class Fast Attack Submarine (SSN)", "Seawolf-Class Fast Attack Submarine (SSN)"]
fixed = ["C-2 Greyhound", "C-130 Hercules", "E-2 Hawkeye", "E-6B Mercury", "EA-6B Prowler", "EA-18G Growler", "EP-3E Aries", "FA-18C", "FA-18D", "FA-18E", "FA-18F", "P-8 Poseidon", "P-3 Orion", "T-6B Texan", "T-45 Goshawk", "F-35B Lightning", "F-35C Lightning", "MV-22 Osprey"]
rotary = ["CH-53 Sea Stallion", "MH-53 Sea Dragon", "MH-60S Seahawk", "MH-60R Seahawk", "TH-57 Sea Ranger", "MV-22 Osprey"]
unmanned = ["MQ-8 Fire Scout", "MQ-8C Fire Scout", "MQ-4C Triton", "X-47B"]
platforms = [ships, subs, fixed, rotary, unmanned]

image = Image

class App(Frame):


    def __init__(self, parent):

        f = open("results.txt", "w")
        Frame.__init__(self, parent, background="white")
        self.count = 0
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

            
        rand = random.randrange(0, 5)
        length = len(platforms[rand])
        rand2 = random.randrange(0, length-1)
        rand3 = random.randrange(1, 5)

        full_name = "images/" + platforms[rand][rand2] + "/" + str(rand3)

        image = Image.open(full_name).resize((800,600))
        photo = ImageTk.PhotoImage(image)

        w = Label(self, image=photo)
        w.photo = photo
        w.pack()

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()

        ray = ["a","b","c","d"]
        v5 = random.randrange(0, length-1)
        text = platforms[rand][v5]
        ray[0] = text

        v6 = random.randrange(0, length-1)
        while(v6 == v5):
            v6 = random.randrange(0, length-1)
        text = platforms[rand][v6]
        ray[1] = text

        v7 = random.randrange(0, length-1)
        while(v7 == v5 or v7 == v6):
            v7 = random.randrange(0, length-1)
        text = platforms[rand][v7]
        ray[2] = text

        ray[3] = platforms[rand][rand2]

        v8 = random.randrange(0,3)
        option_text = ray[v8]
        self.option = Radiobutton(self, text=option_text, variable=v1, value=1).pack(anchor=W)

        v9 = random.randrange(0,3)
        while(v9 == v8):
            v9 = random.randrange(0,3)
        option_text = ray[v9]
        self.option2 = Radiobutton(self, text=option_text, variable=v2, value=2).pack(anchor=W)

        v10 = random.randrange(0,3)
        while(v10 == v8 or v10 == v9):
            v10 = random.randrange(0,3)
        option_text = ray[v10]
        self.option3 = Radiobutton(self, text=option_text, variable=v3, value=3).pack(anchor=W)

        if(v8 != 0 and v9 != 0 and v10 != 0):
            v11 = 0
        if(v8 != 1 and v9 != 1 and v10 != 1):
            v11 = 1
        if(v8 != 2 and v9 != 2 and v10 != 2):
            v11 = 2
        if(v8 != 3 and v9 != 3 and v10 != 3):
            v11 = 3
        option_text = ray[v11]
        self.option4 = Radiobutton(self, text=option_text, variable=v4, value=4).pack(anchor=W)

        self.button = Button(self, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)


    def submit(self):
        self.count += 1
        image.close()
        
        self.starter
        print ("submit")

    def leader(self):
        print ("leaderboard")



root = Tk()

app = App(root)

root.mainloop()