"""
Program s funkciou kruhy(n) nakreslí n dotýkajúcich sa kruhov, ktorých stredy ležia na obvode kružnice. Tieto kruhy zafarbi náhodnými farbami. Zvoľ si vhodné súradnice stredu myslenej kružnice a jej veľkosť.

"""


from tkinter import Canvas, mainloop
from math import radians, cos, sin
from random import randrange


canvas = Canvas()
canvas.pack()

def kruhy(n):
    step = 360/n
    x0, y0 = 150, 130
    r = 100
    
    r_small = r * sin(radians(180/n))

    for i in range(n):
        # mids of the small
        mx = x0 + r * cos(radians(i * step))
        my = y0 + r * sin(radians(i * step))
        canvas.create_oval(mx - r_small, my - r_small, mx + r_small, my + r_small, fill=f"#{randrange(256**3):06x}")


kruhy(14)

mainloop()