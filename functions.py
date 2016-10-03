def createOptionButtons(self):

    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    ray = []
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

    v11 = random.randrange(0,3)
    while(v11 == v8 or v11 == v9 or v11 == v10):
        v11 = random.randrange(0,3)
    option_text = ray[v11]
    self.option4 = Radiobutton(self, text=option_text, variable=v4, value=4).pack(anchor=W)
 
def starter(self):

    self.start.pack_forget()
    self.lead.pack_forget()

    count = 0

    while(count <= 30):
        
        rand = random.randrange(0, 5)
        length = len(platforms[rand])
        rand2 = random.randrange(0, length-1)
        rand3 = random.randrange(1, 5)

        full_name = "images/" + platforms[rand][rand2] + "/" + str(rand3)

        image = Image.open(full_name)
        photo = ImageTk.PhotoImage(image)

        w = Label(self, image=photo)
        w.photo = photo
        w.pack()

        createOptionButtons(self)

        self.button = Button(self, text="SUBMIT", command=self.submit)
        self.button.pack(side=LEFT)