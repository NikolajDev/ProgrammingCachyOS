import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.bind('<ButtonPress>', print)

tkinter.mainloop()