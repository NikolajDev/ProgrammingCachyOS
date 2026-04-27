"""
Napíš program s funkciou ceska_vlajka(sirka, vyska), ktorá nakresli vlajku Českej republiky (vlajku bývalého Československa). V parametroch sirka, vyska má zadané rozmery vlajky. Modrý klin ide do polovice šírky vlajky. Pre volanie ceska_vlajka(300, 200) by si mal dostať takýto výstup:
"""


from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()


def ceska_vlajka(sirka, vyska):
    x = 30
    y = 30
    points = ((x,y), (x+sirka/2, y+vyska/2), (x, y + vyska), (x, y))
    canvas.create_rectangle(x, y, x + sirka, y + vyska/2, fill="white", width=0)
    canvas.create_rectangle(x, y + vyska/2, x + sirka, y + vyska, fill="red", width=0)
    canvas.create_polygon(points, fill="dark blue", width=0)
    canvas.create_rectangle(x, y, x + sirka, y + vyska)

ceska_vlajka(300, 200)

mainloop()