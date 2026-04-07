import tkinter
import random

class Bodka:

    def __init__(self, canvas, x, y):
        self.id = canvas.create_oval(x - 5, y - 5, x + 5, y + 5)
        self.canvas = canvas

    def prefarbi(self):
        if random.randrange(2):
            farba = 'red'
        else:
            farba = 'blue'
        self.canvas.itemconfig(self.id, fill=farba)

canvas = tkinter.Canvas()
canvas.pack()
bodky = []
for i in range(100):
    bodky.append(Bodka(canvas, random.randint(10, 300), random.randint(10, 250)))
for b in bodky:
    b.prefarbi()