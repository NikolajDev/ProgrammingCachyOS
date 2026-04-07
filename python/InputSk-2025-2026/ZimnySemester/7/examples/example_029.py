import tkinter

zoznam = []

def klik(event):
    zoznam[:] = [event.x, event.y]

def tahaj(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(ciara, zoznam)

canvas = tkinter.Canvas()
canvas.pack()
ciara = canvas.create_line(0, 0, 0, 0)
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()