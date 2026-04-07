import tkinter
import random

canvas = Kruh.canvas = Obdlznik.canvas = tkinter.Canvas()
canvas.pack()

sk = Skupina()

for i in range(20):
    if random.randrange(2) == 0:
        sk.pridaj(Kruh(random.randint(50, 200),
                       random.randint(50, 200), 30, 'blue'))
    else:
        sk.pridaj(Obdlznik(random.randint(50, 200),
                           random.randint(50, 200), 40, 40))

sk.prefarbi_typ('kruh', 'yellow')
sk.posun_typ('obdlznik', -10, -25)