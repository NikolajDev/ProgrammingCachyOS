"""
Napíš program s funkciou co_najvacsie(n), ktorá medzi šírku grafickej plochy 10 a 380 vykreslí n čo najväčších rovnako veľkých štvorcov (s medzerou 5). Pre dané n teda najprv vypočítaš veľkosť štvorcov tak, aby boli čo najväčšie a zmestili sa do danej šírky. Štvorce vyplň náhodnými farbami. Napríklad pre co_najvacsie(7) môžeš dostať takýto výstup:

"""

# max width = 380 start on x = 10 so width = 370
# spaces between x+5

from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()

def co_najvacsie(n):
    max_width = (370 - ((n - 1) * 5)) // n
    x = 10
    y = 10
    for _ in range(n):
        color = f"#{randrange(256**3):06x}"  
        canvas.create_rectangle(x, y, x + max_width, y + max_width, fill=color)
        x += max_width + 5
    
co_najvacsie(7)

mainloop()