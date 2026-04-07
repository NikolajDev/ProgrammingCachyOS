import tkinter

class Kruh:
    canvas = None

    def __init__(self, x, y, r, farba='red'):
        self._x, self._y, self._r = x, y, r
        self._farba = farba
        self._id = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

    def __str__(self):
        return f'Kruh({self._x}, {self._y}, {self._r}, {self._farba!r})'

    def posun(self, dx, dy):
        self._x += dx
        self._y += dy
        self.canvas.move(self._id, dx, dy)

    def zmen_r(self, r):
        self._r = r
        self.canvas.coords(self._id,
            self._x - self._r, self._y - self._r,
            self._x + self._r, self._y + self._r)

    def zmen_farbu(self, farba):
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)

class Obdlznik:
    canvas = None

    def __init__(self, x, y, sirka, vyska, farba='red'):
        self._x, self._y, self._sirka, self._vyska = x, y, sirka, vyska
        self._farba = farba
        self._id = self.canvas.create_rectangle(x, y, x+sirka, y+sirka, fill=farba)

    def __str__(self):
        return f'Obdlznik({self._x}, {self._y}, {self._sirka}, {self._vyska}, {self._farba!r})'

    def posun(self, dx, dy):
        self._x += dx
        self._y += dy
        self.canvas.move(self._id, dx, dy)

    def zmen_velkost(self, sirka, vyska):
        self._sirka, self._vyska = sirka, vyska
        self.canvas.coords(self._id,
            self._x, self._y,
            self._x + self._sirka, self._y + self._vyska)

    def zmen_farbu(self, farba):
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)

class Skupina:
    def __init__(self):
        self._zoznam = []

    def pridaj(self, utvar):
        self._zoznam.append(utvar)

    def posun(self, dx, dy):
        for utvar in self._zoznam:
            utvar.posun(dx, dy)

    def posun_typ(self, dx, dy, typ):
        for utvar in self._zoznam:
            if type(utvar) == typ:
                utvar.posun(dx, dy)

    def zmen_farbu(self, farba):
        for utvar in self._zoznam:
            utvar.zmen_farbu(farba)

    def zmen_farbu_typ(self, farba, typ):
        for utvar in self._zoznam:
            if type(utvar) == typ:
                utvar.zmen_farbu(farba)

#----------------------------------------

c = Kruh.canvas = Obdlznik.canvas = tkinter.Canvas()
c.pack()

k = Kruh(50, 50, 30, 'blue')
r = Obdlznik(100, 20, 100, 50)
k.zmen_farbu('green')
r.posun(50, 0)