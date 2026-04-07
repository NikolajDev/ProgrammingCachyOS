import tkinter
import random

def kresli_text(text):
    x = random.randint(50, 330)
    y = random.randint(20, 240)
    canvas.create_text(x, y, text=text)

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    kresli_text('PYTHON')

tkinter.mainloop()