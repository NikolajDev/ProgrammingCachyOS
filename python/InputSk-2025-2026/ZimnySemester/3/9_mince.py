"""
Program s funkciou mince(n) nakreslí n náhodných mincí. Mincami sú farebné kruhy s polomerom 20, v ktorých sú veľké ('arial 30') náhodné číslice od 1 do 9. Napríklad pre volanie mince(30) môžeš dostať niečo podobné:

"""

from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()

def mince(n):
    for i in range(n):
        x = randrange(20, 360) 
        y = randrange(20, 245)

        val = randrange(1, 10)
        color = f'#{randrange(256**3):06x}'

        r = 20

        canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
        canvas.create_text(x, y, text=val, font='arial 30')

mince(30)
mainloop()