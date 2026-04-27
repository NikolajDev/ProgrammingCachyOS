"""
Napíš program s funkciou domceky(n), ktorá nakreslí n náhodných farebných domčekov. Každý domček sa skladá z rovnostranného trojuholníka (použi riešenie z predchádzajúcej úlohy) a štvorca. Polohu domčeka, veľkosť strany jeho štvorca a trojuholníka zvoľ náhodne (veľkosť bude náhodné číslo z <10, 50>). Tiež ich farby zvoľ náhodne. Pre domceky(20) by si mohol dostať takýto výstup:

"""
# size of windows Canvas 380x270

from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()

def domceky(n):
    for _ in range(n):
        a = randrange(10, 51)
        x = randrange(10, 330)
        y = randrange(10, 220)
        pythagor = round((a**2 - ((a/2)**2))**(1/2), 0)
        points = ((x, y), (x+a, y), (x + (a/2), y - pythagor))
        canvas.create_polygon(points, fill=f"#{randrange(256**3):06x}", width=0)
        canvas.create_rectangle(x, y, x+a, y+a,
        fill=f"#{randrange(256**3):06x}", width=0)

domceky(100)

mainloop()