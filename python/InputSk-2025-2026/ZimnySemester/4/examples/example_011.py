import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(100):
    x = random.randint(1, 350)
    y = random.randint(1, 230)
    a = random.randint(1, 30)
    if a <= 10:
        farba = 'red'
    elif a <= 20:
        farba = 'blue'
    else:
        farba = ''
    canvas.create_rectangle(x, y, x + a, y + a, fill=farba)

tkinter.mainloop()