import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(20):
    sirka = random.randint(10, 80)
    vyska = random.randint(10, 80)
    x = random.randint(10, 370 - sirka)
    y = random.randint(10, 260 - vyska)
    canvas.create_rectangle(x, y, x + sirka, y + vyska)

tkinter.mainloop()