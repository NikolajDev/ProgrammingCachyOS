"""
Program s funkciou prechod() nakreslí 25 obdĺžnikov veľkosti 15x250, ktoré sú uložené tesne vedľa seba. Tieto obdĺžniky postupne menia farby od červenej k modrej: čím je väčšie x obdĺžnika tým menej červenej a viac modrej (využi funkciu rgb z prednášky). Mohlo by to vyzerať takto:

"""

from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def prechod():
    r = 255
    g = 0
    b = 0
    step = 255 // 25
    x = 5
    y = 5
    for i in range(25):
        canvas.create_rectangle(x, y, x + 15, y + 250, fill = f"{rgb(r, g, b)}", width = 0)
        x += 15
        r -= step
        b += step

prechod()

mainloop()