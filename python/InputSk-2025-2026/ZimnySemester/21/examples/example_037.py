class Anim:
    canvas = None
    def __init__(self, x, y, zoz, tik=100, dx=0, dy=0):
        ...

    def pohyb(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        self.canvas.itemconfig(self.id, image=self.zoz[self.faza])
        if self.dx or self.dy:
            self.presun((self.x + self.dx) % self.sirka,
                        (self.y + self.dy) % self.vyska)

    ...

class AnimSOdrazom(Anim):
    def pohyb(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        self.canvas.itemconfig(self.id, image=self.zoz[self.faza])
        if self.dx or self.dy:
            if self.x+self.dx < self.vel: self.dx = abs(self.dx)
            if self.y+self.dy < self.vel: self.dy = abs(self.dy)
            if self.x+self.dx > self.sirka - self.vel: self.dx = -abs(self.dx)
            if self.y+self.dy > self.vyska - self.vel: self.dy = -abs(self.dy)
            self.presun(self.x + self.dx, self.y + self.dy)