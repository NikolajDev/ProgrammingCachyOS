"""
Podobná úloha ako v predchádzajúcom príklade, len v tomto sa využívajú uhlopriečky štvorca. Asi tu budeš vedieť využiť podmienky x < y alebo 300 - x < y. Funkcia uhlopriecky(n=4000) vykresli 4000 farebných bodiek:

"""

from tkinter import Canvas, mainloop
from random import randint

canvas = Canvas()
canvas.pack()

def uhlopriecky(n=4000):
    for i in range(n):
        x = randint(1, 300)
        y = randint(1, 300)
        if x < y and 300 - x < y:
            farba = 'green'
        elif 300 - x < y:
            farba = 'yellow'
        elif 300 - x > y and x > y:
            farba = 'blue'
        else:
            farba = 'red'
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

uhlopriecky()

mainloop()