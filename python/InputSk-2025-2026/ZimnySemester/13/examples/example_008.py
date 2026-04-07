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

    def zmen_r(self, r):
        self._r = r
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def zmen_farba(self, farba):
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)

    def zmen_x(self, x):
        self._x = x
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def zmen_y(self, y):
        self._y = y
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def daj_r(self):
        return self._r

    def daj_farba(self):
        return self._farba

    def daj_x(self):
        return self._x

    def daj_y(self):
        return self._y

    x = property(daj_x, zmen_x)
    y = property(daj_y, zmen_y)
    r = property(daj_r, zmen_r)
    farba = property(daj_farbu, zmen_farbu)