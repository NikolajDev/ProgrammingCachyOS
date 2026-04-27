"""
Napíš program s funkciou cikcak(n, x, y, d), ktorá nakreslí cikcakovú čiaru zloženú z n úsečiek. V parametroch x, y má nastavené súradnice najľavejšieho bodu prvej úsečky a v d je posunutie pre x aj y každého ďalšieho bodu čiary. Zrejme k y sa to raz pripočíta a raz odpočíta. Napríklad pre volanie cikcak(16, 10, 100, 20) by si mal dostať:

"""
from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def cikcak(n, x, y, d):
    num = 1
    for i in range(n):
        canvas.create_line(x, y, x+d, y+(d*num), width=2, fill="blue")
        y = y+(d*num)
        x = x+d
        num *= (-1)

cikcak(16, 10, 100, 20)
mainloop()
