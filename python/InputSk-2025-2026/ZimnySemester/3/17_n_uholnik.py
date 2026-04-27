"""
Program s funkciou n_uholnik(n, a, x, y) pre dané n a dĺžku strany a nakreslí pravidelný n-uholník so stranou a. Využi body na kružnici so stredom x a y a polomerom r, ktorý budeš ale musieť vypočítať. Napríklad pre n_uholnik(7, 100, 180, 130) nakreslíš:

"""

from tkinter import Canvas, mainloop
from math import radians, cos, sin


canvas = Canvas()
canvas.pack()

def n_uholnik(n, a, x, y):
    step = 360/n
    angle = 180/n

    r = a / (2 * sin(radians(angle)))

    x0 = x + r * cos(radians(0))
    y0 = y + r * sin(radians(0))

    for i in range(1, n + 1):
        x1 = x + r * cos(radians(step * i))
        y1 = y + r * sin(radians(step * i))
        canvas.create_line(x0, y0, x1, y1, width=3)
        x0, y0 = x1, y1

n_uholnik(7, 100, 180, 130)

mainloop()