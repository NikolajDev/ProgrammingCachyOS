import tkinter
from PIL import Image, ImageTk

class Plocha:
    def __init__(self, meno_pozadia):
        self.pozadie = tkinter.PhotoImage(file=meno_pozadia)
        sir, vys = self.pozadie.width(), self.pozadie.height()
        self.canvas = Anim.canvas = tkinter.Canvas(width=sir, height=vys)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.pozadie, anchor='nw')
        self.zoz = strihaj('vtak.png', 8)
        self.azoz = []
        self.timer()
        self.canvas.bind('<ButtonPress>', self.klik)

    ...

...

win = tkinter.Tk()
Plocha('les.png')