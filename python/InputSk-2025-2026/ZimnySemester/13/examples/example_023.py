class Kruh(Utvar):
    def __init__(self, x, y, r, farba='red'):
        super().__init__(x, y, farba)
        self._r = r
        self._id = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)

    def zmen_r(self, r):
        self._r = r
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

class Obdlznik(Utvar):
    def __init__(self, x, y, sirka, vyska, farba='red'):
        super().__init__(x, y, farba)
        self._sirka, self._vyska = sirka, vyska
        self._id = self.canvas.create_rectangle(x, y, x + sirka, y + sirka, fill=farba)

    def zmen_velkost(self, sirka, vyska):
        self._sirka, self._vyska = sirka, vyska
        self.canvas.coords(self._id,
            self._x, self._y,
            self._x + self._sirka, self._y + self._vyska)