"""
Program s funkciou vypis(text) postupne každé písmeno tohto textu zapíše ('arial 26') do jedného farebného štvorca veľkosti 30x30. Tieto štvorce sú umiestnené tesne vedľa seba. Farby štvorcov aj písmen zvoľ náhodne. Napríklad pre volanie vypis('LUBIM PYTHON')) môžeš dostať niečo podobné:

"""

from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()

def vypis(text):
    x = 15
    y = 115
    r = 13
    for i in text:
        color = f"#{randrange(256**3):06x}"
        canvas.create_rectangle(x - r, y - r, x + r, y + r, fill = color)
        color = f"#{randrange(256**3):06x}"
        canvas.create_text(x, y, text=i, font = "arial 22", fill = color)
        x += 2*r

vypis('LUBIM ANDREJKU')

mainloop()