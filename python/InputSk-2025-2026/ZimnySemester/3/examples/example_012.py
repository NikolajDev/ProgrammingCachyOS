import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 30
sirka, vyska = 140, 80
canvas.create_rectangle(x, y, x + sirka, y + vyska)

tkinter.mainloop()