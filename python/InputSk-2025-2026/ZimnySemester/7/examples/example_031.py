import tkinter
import random

zoznam = []

def klik(event):
    global poly
    zoznam[:] = [event.x, event.y]
    farba = f'#{random.randrange(256**3):06x}'
    poly = canvas.create_polygon(0, 0, 0, 0, fill=farba)

def tahaj(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(poly, zoznam)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()