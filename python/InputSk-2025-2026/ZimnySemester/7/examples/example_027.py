import tkinter

def klik(event):
    canvas.create_line(100, 200, event.x, event.y, fill='red', width=3)

def tahaj(event):
    canvas.create_line(100, 200, event.x, event.y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', tahaj)

tkinter.mainloop()