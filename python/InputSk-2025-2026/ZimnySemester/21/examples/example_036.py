class Plocha:
    ...

    def klik(self, event):
        ix = random.randrange(len(self.zoz))
        if ix == 0:
            dx, dy = random.randint(1, 5), random.randint(-2, 2)
        elif ix == 1:
            dx, dy = random.randint(-7, -4), random.randint(-2, 2)
        elif ix == 2:
            dx, dy = random.randint(-5, 5), random.randint(-5, 5)
        a = Anim(event.x, event.y, self.zoz[ix], random.randint(20, 200), dx, dy)
        if ix == 2:
            a.odraz = True
        self.azoz.append(a)

    ...