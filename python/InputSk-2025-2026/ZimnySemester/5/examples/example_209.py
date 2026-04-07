a = (70, 150)
b = (200, 200)
c = (150, 250)
d = (120, 70)
e = (50, 220)

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_polygon(a, b, c, d, fill='red')