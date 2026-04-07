class Utvar:
    canvas = tkinter.Canvas(width=400, height=400)
    canvas.pack()

    def __init__(self, x, y, farba='red'):
        self._x, self._y, self._farba = x, y, farba
        self._id = None

    def posun(self, dx, dy):
        self._x += dx
        self._y += dy
        self.canvas.move(self._id, dx, dy)

    def zmen_farbu(self, farba):
        self._farba = farba
        self.canvas.itemconfig(self._id, fill=farba)