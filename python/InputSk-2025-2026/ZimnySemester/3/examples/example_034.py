import tkinter
import random

def nahodna_farba():
    return f'#{random.randrange(256**3):06x}'

def kruznica(r, x, y, fill=''):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill)

canvas = tkinter.Canvas()
canvas.pack()

for i in range(100):
    x = random.randint(20, 350)
    y = random.randint(20, 240)
    kruznica(20, x, y, nahodna_farba())

tkinter.mainloop()