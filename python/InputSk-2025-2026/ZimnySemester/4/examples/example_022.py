import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if random.randrange(50):             # t.j. random.randrange(50) != 0
        farba = 'red'
    else:
        farba = 'blue'
    canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

tkinter.mainloop()