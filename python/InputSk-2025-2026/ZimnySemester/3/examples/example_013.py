import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    x = random.randint(10, 240)
    y = random.randint(10, 180)
    sirka, vyska = 140, 80
    canvas.create_rectangle(x, y, x + sirka, y + vyska)

tkinter.mainloop()