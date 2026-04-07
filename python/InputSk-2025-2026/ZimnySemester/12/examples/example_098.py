import tkinter

class Obdlznik:
    canvas = None

    def __init__(self, x, y, sirka, vyska, farba='red'):
        self.x, self.y = x, y
        self.sirka, self.vyska = sirka, vyska
        self.farba = farba
        self.id = self.canvas.create_rectangle(x, y,
                                               x + sirka, y + vyska,
                                               fill=farba)

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, sirka, vyska):
        self.sirka, self.vyska = sirka, vyska
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x + sirka, self.y + vyska)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=farba)

Obdlznik.canvas = tkinter.Canvas()
Obdlznik.canvas.pack()
r1 = Obdlznik(50, 50, 50, 30, 'blue')
r2 = Obdlznik(150, 100, 80, 80)