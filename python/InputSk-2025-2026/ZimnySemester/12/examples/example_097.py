import tkinter

class Kruh:
    canvas = None

    def __init__(self, x, y, r, farba='red'):
        self.x, self.y, self.r = x, y, r
        self.farba = farba
        self.id = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=farba)

Kruh.canvas = tkinter.Canvas()
Kruh.canvas.pack()
k1 = Kruh(50, 50, 30, 'blue')
k2 = Kruh(150, 100, 80)

k1.posun(30,10)
k2.zmen(50)
k1.prefarbi('green')