class Plocha:
    def __init__(self, meno_pozadia, *obrazky):
        self.pozadie = tkinter.PhotoImage(file=meno_pozadia)
        sir, vys = self.pozadie.width(), self.pozadie.height()
        Anim.sirka, Anim.vyska = sir, vys
        ...

    def timer(self):
        teraz = time.time()
        for a in self.azoz:
            if a.time < teraz:
                a.pohyb()
                a.time = teraz + a.tik
        self.canvas.after(20, self.timer)

    ...

    def klik(self, event):
        ix = random.randrange(len(self.zoz))
        if ix == 0:
            dx, dy = random.randint(1, 5), random.randint(-2, 2)
        elif ix == 1:
            dx, dy = random.randint(-7, -4), random.randint(-2, 2)
        elif ix == 2:
            dx, dy = random.randint(-5, 5), random.randint(-5, 5)
        a = Anim(event.x, event.y, self.zoz[ix], random.randint(20, 200), dx, dy)
        self.azoz.append(a)

    ...