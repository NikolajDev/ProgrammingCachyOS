import tkinter
from math import sin, cos, radians

canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 150, 130
r = 110

text = input('zadaj text: ')
n = len(text)
uhol, posun = 0, 360 / n

for znak in text:
    x = x0 + r * cos(radians(uhol))
    y = y0 + r * sin(radians(uhol))
    canvas.create_text(x, y, text=znak)
    uhol += posun

tkinter.mainloop()