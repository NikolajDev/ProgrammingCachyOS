class Anim:
    ...

    def pohyb(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        self.canvas.itemconfig(self.id, image=self.zoz[self.faza])
        if self.dx or self.dy:
            self.presun((self.x + self.dx) % self.sirka,
                        (self.y + self.dy) % self.vyska)