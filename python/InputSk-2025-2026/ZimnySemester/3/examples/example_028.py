import tkinter
import random

def nahodna_farba():
    return f'#{random.randrange(256**3):06x}'

def stvorec(strana, x, y, farba=''):
    canvas.create_rectangle(x, y, x + strana, y - strana, fill=farba)

canvas = tkinter.Canvas()
canvas.pack()

x, y = 5, 200
for strana in range(10, 90, 10):
    stvorec(strana, x, y, nahodna_farba())
    x += strana + 1

tkinter.mainloop()