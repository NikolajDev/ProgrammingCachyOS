import tkinter
import random
from PIL import Image, ImageTk

class Plocha:
    def __init__(self, meno_pozadia, *obrazky):
        self.pozadie = tkinter.PhotoImage(file=meno_pozadia)
        sir, vys = self.pozadie.width(), self.pozadie.height()
        self.canvas = Anim.canvas = tkinter.Canvas(width=sir, height=vys)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.pozadie, anchor='nw')
        self.zoz = obrazky
        self.azoz = []
        self.timer()
        self.canvas.bind('<ButtonPress>', self.klik)

    def timer(self):
        for a in self.azoz:
            a.dalsia_faza()
        self.canvas.after(100, self.timer)

    def klik(self, event):
        self.azoz.append(Anim(event.x, event.y, random.choice(self.zoz)))