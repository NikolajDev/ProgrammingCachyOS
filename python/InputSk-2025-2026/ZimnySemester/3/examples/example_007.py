import tkinter
import random

def vypis_cislo(i):
    x = random.randint(50, 330)
    y = random.randint(20, 240)
    canvas.create_text(x, y, text=i)

canvas = tkinter.Canvas()
canvas.pack()

for i in range(50):
    vypis_cislo(i)

tkinter.mainloop()