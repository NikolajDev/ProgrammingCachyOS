import tkinter
import random
import math

def vzd(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def kresli_bodku(x, y, farba):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

def farebne_bodky(pocet):
    for i in range(pocet):
        x = random.randint(10, 290)
        y = random.randint(10, 290)
        if vzd(x, y, 150, 150) > 100:
            kresli_bodku(x, y, 'navy')
        elif vzd(x, y, 230, 150) > 100:
            kresli_bodku(x, y, 'red')
        else:
            kresli_bodku(x, y, 'yellow')

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

farebne_bodky(5000)

tkinter.mainloop()