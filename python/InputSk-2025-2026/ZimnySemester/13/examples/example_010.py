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

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        self._r = r
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    @property
    def farba(self):
        return self._farba

    @farba.setter
    def farba(self, farba):
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)