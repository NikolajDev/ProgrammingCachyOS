import tkinter

def klik(event):
    global xx, yy
    xx, yy = event.x, event.y

def tahaj(event):
    canvas.create_line(xx, yy, event.x, event.y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()