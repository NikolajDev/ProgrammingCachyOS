"""
Napíš program s funkciou olympijske(x, y, r, dx, dy), ktorá nakreslí olympijské kruhy. V parametroch x, y, r, dx, dy má zadané: súradnice stredu horného najľavejšieho kruhu (x, y), polomer kruhov (r) a vzdialenosť medzi kruhmi v jednom rade (dx) a vzdialenosť medzi radmi (dy). Hrúbka čiar kružníc nech je 15. Pre volanie olympijske(70, 100, 50, 120, 60) by si mal dostať takýto výstup:

"""

from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def olympijske(x, y, r, dx, dy):
    c1, c2, c3, c4, c5 = "blue", "yellow", "black", "green", "red"
    y_dir = 1
    for _ in range(5):
        canvas.create_oval(x - r, y - r, x + r, y + r, outline = c1, width=15)
        c1, c2, c3, c4, c5 = c2, c3, c4, c5, c1
        x += dx/2
        y += (dy * y_dir)
        y_dir *= (-1)
    
olympijske(70, 100, 50, 120, 60)

mainloop()