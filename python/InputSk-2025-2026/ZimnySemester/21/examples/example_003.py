import tkinter
from PIL import Image, ImageTk

class Anim:
    def __init__(self, x, y, zoz):
        self.id = canvas.create_image(x, y)
        self.zoz = zoz
        self.faza = 0

    def dalsia_faza(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        canvas.itemconfig(self.id, image=self.zoz[self.faza])

def strihaj(meno_suboru, n):
    obr = Image.open(meno_suboru)
    sir, vys = obr.width // n, obr.height
    return [ImageTk.PhotoImage(obr.crop((x, 0, x + sir, vys)))
                for x in range(0, obr.width, sir)]

canvas = tkinter.Canvas()
canvas.pack()

zoz = strihaj('vtak.png', 8)
a1 = Anim(200, 120, zoz)
a2 = Anim(100, 80, zoz)
a3 = Anim(300, 100, zoz)
while True:
    a1.dalsia_faza()
    a2.dalsia_faza()
    a3.dalsia_faza()
    canvas.update()
    canvas.after(100)