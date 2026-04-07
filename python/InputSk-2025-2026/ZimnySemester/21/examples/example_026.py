class Anim:
    canvas = None
    def __init__(self, x, y, zoz, tik=100):
        self.tik = tik / 1000
        self.time = time.time() + self.tik
        ...