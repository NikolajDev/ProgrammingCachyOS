class Kruh:
    canvas = tkinter.Canvas()
    canvas.pack()

    def __init__(self, x, y, r, farba='red'):
        self._x, self._y, self._r = x, y, r
        self._farba = farba
        self._id = self.canvas.create_oval(
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r,
            fill=farba)

    def __str__(self):
        return f'Kruh({self._x}, {self._y}, {self._r}, {self._farba!r})'

    def posun(self, dx=0, dy=0):
        self._x += dx
        self._y += dy
        self.canvas.move(self._id, dx, dy)

    def zmen_r(self, r):               # setter
        self._r = r
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def zmen_farba(self, farba):       # setter
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)

    def zmen_x(self, x):               # setter
        self._x = x
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def zmen_y(self, y):               # setter
        self._y = y
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def daj_r(self):                   # getter
        return self._r

    def daj_farba(self):               # getter
        return self._farba

    def daj_x(self):                   # getter
        return self._x

    def daj_y(self):                   # getter
        return self._y