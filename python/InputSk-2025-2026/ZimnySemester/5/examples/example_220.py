import tkinter
import random

canvas = tkinter.Canvas(bg='white')
canvas.pack()

poly = canvas.create_polygon(0, 0, 0, 0, fill='yellow', outline='blue')
krivka = []
for i in range(100):
    bod = [random.randrange(350), random.randrange(250)]
    krivka.extend(bod)     # to isté ako    krivka += bod
    canvas.coords(poly, krivka)
    canvas.update()
    canvas.after(300)

tkinter.mainloop()