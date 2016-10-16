from __future__ import print_function
from tkinter import *
from PIL import Image, ImageTk
import random

ships = ["Arleigh Burke Class Destroyer (DDG-51)", "Zumwalt Class Destroyer (DDG-1000)", "Cruiser (CG)", "Littoral Combat Ship (LCS)", "Dock Landing Ship (LSD)", "Landing Helicopter Assault (LHA)", "Landing Helicopter Dock (LHD)", "Aircraft Carrier (CVN)", "Amphibious Command Ship (LCC)", "Amphibious Transport Dock (LPD)", "Landing Craft Air Cushion (LCAC)", "Mine Counter Measures (MCM)", "Patrol Coastal Ship (PC)", "Submarine Tender (AS)"]
subs = ["Ohio-Class Ballistic or Guided Missile Submarine (SSBN or SSGN)", "Virginia-Class Fast Attack Submarine (SSN)", "Los Angeles-Class Fast Attack Submarine (SSN)", "Seawolf-Class Fast Attack Submarine (SSN)"]
fixed = ["C-2 Greyhound", "C-130 Hercules", "E-2 Hawkeye", "E-6B Mercury", "EA-6B Prowler", "EA-18G Growler", "EP-3E Aries", "FA-18C", "FA-18D", "FA-18E", "FA-18F", "P-8 Poseidon", "P-3 Orion", "T-6B Texan", "T-45 Goshawk", "F-35B Lightning", "F-35C Lightning", "MV-22 Osprey"]
rotary = ["CH-53 Sea Stallion", "MH-53 Sea Dragon", "MH-60S Seahawk", "MH-60R Seahawk", "TH-57 Sea Ranger", "MV-22 Osprey"]
unmanned = ["MQ-8 Fire Scout", "MQ-8C Fire Scout", "MQ-4C Triton", "X-47B"]
platforms = [ships, subs, fixed, rotary, unmanned]
correct_answers = [None] * 30
user_answers = [None] * 30

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

        self.quiz()

    def quiz(self):

        randlist = [platforms[0]] * 30 + [platforms[1]] * 25 + [platforms[2]] * 20 + [platforms[3]] * 20 + [platforms[4]] * 5
        rand1 = random.choice(randlist)

        rand = 0

        for b in platforms:
            if(rand1 == b):
                if(b == ships):
                    rand = 0
                if(b == subs):
                    rand = 1
                if(b == fixed):
                    rand = 2
                if(b == rotary):
                    rand = 3
                if(b == unmanned):
                    rand = 4

        length = len(platforms[rand])
        rand2 = random.randint(0, length-1)
        rand3 = random.randint(1, 5)

        self.answer = platforms[rand][rand2]
        correct_answers[self.count] = self.answer
        print(correct_answers[self.count])
        full_name = "images/" + self.answer + "/" + str(rand3)

        self.image = Image.open(full_name).resize((640,480))
        photo = ImageTk.PhotoImage(self.image)

        self.w = Label(self, image=photo)
        self.w.photo = photo
        self.w.pack()

        self.v1 = StringVar()

        ray = ["a","b","c","d"]
        v5 = random.randint(0, length-1)
        while(v5 == rand2):
            v5 = random.randint(0, length-1)
        text = platforms[rand][v5]
        ray[0] = text

        v6 = random.randint(0, length-1)
        while(v6 == v5 or v6 == rand2):
            v6 = random.randint(0, length-1)
        text = platforms[rand][v6]
        ray[1] = text

        if(v5 != 0 and v6 != 0 and rand2 != 0):
            v7 = 0
        if(v5 != 1 and v6 != 1 and rand2 != 1):
            v7 = 1
        if(v5 != 2 and v6 != 2 and rand2 != 2):
            v7 = 2
        if(v5 != 3 and v6 != 3 and rand2 != 3):
            v7 = 3
        text = platforms[rand][v7]
        ray[2] = text

        ray[3] = platforms[rand][rand2]

        v8 = random.randint(0,3)
        option_text = ray[v8]
        self.option = Radiobutton(self, text=option_text, variable=self.v1, value=option_text)
        self.option.pack(anchor=W)

        v9 = random.randint(0,3)
        while(v9 == v8):
            v9 = random.randint(0,3)
        option_text2 = ray[v9]
        self.option2 = Radiobutton(self, text=option_text2, variable=self.v1, value=option_text2)
        self.option2.pack(anchor=W)

        v10 = random.randint(0,3)
        while(v10 == v8 or v10 == v9):
            v10 = random.randint(0,3)
        option_text3 = ray[v10]
        self.option3 = Radiobutton(self, text=option_text3, variable=self.v1, value=option_text3)
        self.option3.pack(anchor=W)

        if(v8 != 0 and v9 != 0 and v10 != 0):
            v11 = 0
        if(v8 != 1 and v9 != 1 and v10 != 1):
            v11 = 1
        if(v8 != 2 and v9 != 2 and v10 != 2):
            v11 = 2
        if(v8 != 3 and v9 != 3 and v10 != 3):
            v11 = 3

        option_text4 = ray[v11]
        self.option4 = Radiobutton(self, text=option_text4, variable=self.v1, value=option_text4)
        self.option4.pack(anchor=W)

        self.button = Button(self, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)

    def submit(self):
        self.w.pack_forget()
        self.button.pack_forget()

        self.option.pack_forget()
        self.option2.pack_forget()
        self.option3.pack_forget()
        self.option4.pack_forget()

        if(self.count != 29):
            user_answers[self.count] = self.v1.get()
            print(user_answers[self.count])
            self.quiz()

        else:
            user_answers[29] = self.v1.get()
            self.calc_score()
            self.count = 0
        
        self.count += 1

    def calc_score(self):
        self.score = 0
        counter = 0

        for ans in correct_answers:
            if(user_answers[counter] == ans):
                self.score += 1
            counter += 1
        print(self.score)

    def leader(self):
        print ("leaderboard")



root = Tk()

app = App(root)

root.mainloop()