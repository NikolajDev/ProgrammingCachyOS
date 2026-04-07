import tkinter

canvas = tkinter.Canvas()
canvas.pack()

obr = tkinter.PhotoImage(file='pyton.png')
for x in range(80, 380, 120):
    canvas.create_image(x, 150, image=obr)

tkinter.mainloop()