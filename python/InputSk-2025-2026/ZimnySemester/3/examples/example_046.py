import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

x, y = 10, 120

for i in range(37):
    x1 = x + 10
    y1 = y + random.randint(-10, 10)
    canvas.create_line(x, y, x1, y1, width=3)
    x, y = x1, y1