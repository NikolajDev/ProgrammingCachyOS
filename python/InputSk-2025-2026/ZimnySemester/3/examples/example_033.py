import tkinter

def kruznica(r, x, y):
    canvas.create_oval(x - r, y - r, x + r, y + r)

canvas = tkinter.Canvas()
canvas.pack()

kruznica(80, 150, 100)
canvas.create_text(150, 100, text='+')

tkinter.mainloop()