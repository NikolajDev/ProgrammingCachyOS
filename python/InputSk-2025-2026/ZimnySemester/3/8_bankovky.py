"""
Napíš program s funkciou bankovky(n), ktorá pod seba vygeneruje n bankoviek s náhodnými hodnotami. Na generovanie náhodnej hodnoty použi zápis:

hodnota = random.choice((1, 2, 5, 10, 20, 50))
pomocou ktorého sa náhodne vyberie jedno číslo zo zadanej postupnosti. Program na záver spočíta výslednú sumu. Veľkosť obdĺžnikov nech je 50x20. Napríklad volanie bankovky(10) môžeš dostať takýto výstup:

"""

from tkinter import Canvas, mainloop
from random import choice

canvas = Canvas()
canvas.pack()

def bankovky(n):
    together = 0
    y = 20
    x = 100
    for i in range(n):
        value = choice((1, 2, 5, 10, 20, 50))
        together += value
        canvas.create_rectangle(x, y, x + 50, y + 20, fill="white")
        canvas.create_text(x + 25, y+10, text=f"{value} $", font="Arial 15")
        y+= 22
    canvas.create_text(250, 60, text=f"together = {together}$", font="Arial 15")

bankovky(10)

mainloop()