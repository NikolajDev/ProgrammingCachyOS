import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = Kruh(70, 200, 100)
a.farba = 'yellow'
b = Kruh(10, 180, 80)
c = Kruh(10, 220, 80)
kresli_kruh(a)
kresli_kruh(b)
kresli_kruh(c)

tkinter.mainloop()