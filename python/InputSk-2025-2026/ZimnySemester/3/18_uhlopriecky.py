"""
Program s funkciou uhlopriecky(n, x, y, r) pre dané n nakreslí pravidelný n-uholník, ale dokreslí do neho aj všetky uhlopriečky. Pre volanie uhlopriecky(7, 180, 130, 125) dostaneš:

"""

from tkinter import Canvas, mainloop
from math import radians, cos, sin

canvas = Canvas(width=400, height=400)
canvas.pack()

def uhlopriecky(n, x, y, r):
    step = 360 / n
    
    for i in range(n):
        angle1 = i * step
        x1 = x + r * cos(radians(angle1))
        y1 = y + r * sin(radians(angle1))
        
        for j in range(i + 1, n):
            angle2 = j * step
            x2 = x + r * cos(radians(angle2))
            y2 = y + r * sin(radians(angle2))
            
            canvas.create_line(x1, y1, x2, y2)

uhlopriecky(7, 180, 130, 125)

mainloop()