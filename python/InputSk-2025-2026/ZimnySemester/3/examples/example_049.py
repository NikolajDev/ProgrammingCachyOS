import tkinter
from math import sin, cos, radians

canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 150, 130
r = 110

for uhol in range(0, 360, 15):
    x = x0 + r * cos(radians(uhol))
    y = y0 + r * sin(radians(uhol))
    canvas.create_line(x0, y0, x, y)
    canvas.create_text(x, y, text=uhol)

tkinter.mainloop()