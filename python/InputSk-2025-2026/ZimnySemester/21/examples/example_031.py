class Anim:
    canvas = None
    def __init__(self, x, y, zoz, tik=100, dx=0, dy=0):
        self.tik = tik
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        ...