import tkinter

class Kruh:

    def __init__(self, r, x, y, farba='blue'):
        self.r = r
        self.x = x
        self.y = y
        self.farba = farba

    def vypis(self):
        print(f'Kruh({self.r}, {self.x}, {self.y}, {self.farba!r})')

    def kresli(self):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.farba)

canvas = tkinter.Canvas()
canvas.pack()

a = Kruh(70, 200, 100, 'yellow')
b = Kruh(10, 180, 80)
c = Kruh(10, 220, 80)

zoznam = [a, b, c]
for k in zoznam:
    k.kresli()
for k in zoznam:
    k.vypis()

tkinter.mainloop()