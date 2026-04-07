import tkinter
import random

class Bodka:
    canvas = None
    pocet_modrych = pocet_cervenych = 0

    def __init__(self, x, y):
        self.id = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5)

    def prefarbi(self):
        if random.randrange(2):
            farba = 'red'
            Bodka.pocet_cervenych += 1
        else:
            farba = 'blue'
            Bodka.pocet_modrych += 1
        self.canvas.itemconfig(self.id, fill=farba)

Bodka.canvas = tkinter.Canvas()
Bodka.canvas.pack()
bodky = []
for i in range(100):
    bodky.append(Bodka(random.randint(10, 300), random.randint(10, 250)))
for b in bodky:
    b.prefarbi()
print('pocet modrych =', Bodka.pocet_modrych)
print('pocet cervenych =', Bodka.pocet_cervenych)