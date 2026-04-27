"""
Napíš program s funkciou rovnostranny(x, y, a=280), ktorá pomocou canvas.create_polygon nakreslí rovnostranný trojuholník. V parametroch x, y, a má nastavené súradnice ľavého dolného vrcholu a veľkosť strany trojuholníka. Pre volanie rovnostranny(50, 250) by si mal dostať takýto výstup:

"""

from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def rovnostranny(x, y, a=280):
    pythagor = round((a**2 - ((a/2)**2))**(1/2), 0)
    points = ((x, y), (x+a, y), (x + (a/2), y - pythagor))
    canvas.create_polygon(points, fill="blue")

rovnostranny(50, 250)

mainloop()