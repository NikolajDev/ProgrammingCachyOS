class Kruh:
    canvas = tkinter.Canvas()
    canvas.pack()

    def __init__(self, x, y, r, farba='red'):
        self.x, self.y, self.r = x, y, r
        self.farba = farba
        self.id = self.canvas.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=farba)

    def __str__(self):
        return f'Kruh({self.x}, {self.y}, {self.r}, {self.farba!r})'

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen_r(self, r):
        self.r = r
        self.canvas.coords(self.id,
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r)

    def zmen_farba(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=farba)

    def zmen_x(self, x):
        self.x = x
        self.canvas.coords(self.id,
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r)

    def zmen_y(self, y):
        self.y = y
        self.canvas.coords(self.id,
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r)