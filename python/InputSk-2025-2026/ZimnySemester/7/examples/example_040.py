import tkinter
import random

def kresli():
    x = random.randint(10, 370)
    y = random.randint(10, 250)
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')
    #canvas.update()               # v časovači by sa nemalo volať
    canvas.after(100, kresli)

canvas = tkinter.Canvas()
canvas.pack()

kresli()             # naštartovanie časovača
print('hotovo')

tkinter.mainloop()