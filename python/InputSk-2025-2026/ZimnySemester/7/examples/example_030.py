import tkinter

zoznam = []

def klik(event):
    global ciara
    zoznam[:] = [event.x, event.y]
    ciara = canvas.create_line(0, 0, 0, 0)

def tahaj(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(ciara, zoznam)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()