class Plocha:
    def __init__(self, meno_pozadia, *obrazky):
        ...
        self.tahany = None
        self.canvas.bind('<ButtonPress-3>', self.klik)
        self.canvas.bind('<ButtonPress-1>', self.mouse_down)
        self.canvas.bind('<B1-Motion>', self.mouse_move)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_up)

    ...

    def mouse_down(self, event):
        for a in reversed(self.azoz):
            if a.vnutri(event.x, event.y):
                self.tahany = a
                self.dx, self.dy = event.x - a.x, event.y - a.y
                return
        self.tahany = None

    def mouse_move(self, event):
        if self.tahany is not None:
            self.tahany.presun(event.x-self.dx, event.y-self.dy)

    def mouse_up(self, event):
        self.tahany = None