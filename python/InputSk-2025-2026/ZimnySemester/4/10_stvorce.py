"""
Využi program z prednášky, v ktorom sa vykresľovalo 1000 farebných bodiek (malé krúžky s polomerom 5 bez obrysu) podľa toho či mali x-ovú, alebo y-ovú súradnicu menšiu alebo väčšiu ako 150. Veľkosť grafickej plochy bola 300x300. Zmeň v tomto programe sériu príkazov if tak, aby kreslené bodky vytvorili vnútorný červený štvorec s rozmermi 150x150. Funkcia stvorce(n=4000) vykresli 4000 farebných bodiek:

"""

from tkinter import Canvas, mainloop
from random import randint

canvas = Canvas()
canvas.pack()

def stvorce(n=4000):
    for i in range(n):
        x = randint(1, 300)
        y = randint(1, 300)
        if 75 < x < 225 and 75 < y < 225:
            farba = 'red'
        else:
            farba = 'blue'
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

stvorce()

mainloop()
