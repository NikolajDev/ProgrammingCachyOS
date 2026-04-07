import tkinter
from PIL import Image, ImageTk

class Plocha:
    def __init__(self):
        self.canvas = Anim.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.zoz = strihaj('vtak.png', 8)
        self.azoz = []
        self.timer()
        self.canvas.bind('<ButtonPress>', self.klik)

    def timer(self):
        for a in self.azoz:
            a.dalsia_faza()
        self.canvas.after(100, self.timer)

    def klik(self, event):
        self.azoz.append(Anim(event.x, event.y, self.zoz))

class Anim:
    canvas = None
    def __init__(self, x, y, zoz):
        self.id = self.canvas.create_image(x, y)
        self.zoz = zoz
        self.faza = 0

    def dalsia_faza(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        self.canvas.itemconfig(self.id, image=self.zoz[self.faza])

def strihaj(meno_suboru, n):
    obr = Image.open(meno_suboru)
    sir, vys = obr.width // n, obr.height
    return [ImageTk.PhotoImage(obr.crop((x, 0, x + sir, vys)))
                for x in range(0, obr.width, sir)]

Plocha()