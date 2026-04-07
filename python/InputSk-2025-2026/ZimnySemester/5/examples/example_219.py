import tkinter
import random

canvas = tkinter.Canvas(bg='white')
canvas.pack()

krivka = []
for i in range(30):
    krivka.append((random.randrange(350), random.randrange(250)))
canvas.create_line(krivka)

tkinter.mainloop()