import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(10):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    a = random.randint(5, 50)

    if random.randrange(2):         # t.j. random.randrange(2) != 0
        canvas.create_oval(x - a, y - a, x + a, y + a)
    else:
        canvas.create_rectangle(x - a, y - a, x + a, y + a)

tkinter.mainloop()