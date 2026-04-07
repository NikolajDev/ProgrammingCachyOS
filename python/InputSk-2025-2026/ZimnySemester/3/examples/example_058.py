from tkinter import Canvas, mainloop
from random import randint, randrange
from math import sin, cos, radians

canvas = Canvas()
canvas.pack()

a = 30
n = 100

for i in range(n):
    x1 = randint(a, 380 - a)
    y1 = randint(a, 260 - a)
    uhol = randint(0, 360)
    x2 = x1 + a * cos(radians(uhol))
    y2 = y1 + a * sin(radians(uhol))
    uhol = uhol - 60
    x3 = x1 + a * cos(radians(uhol))
    y3 = y1 + a * sin(radians(uhol))
    farba = f'#{randrange(256**3):06x}'
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=farba)

mainloop()