class Anim:
    canvas = None
    def __init__(self, x, y, zoz):
        self.x, self.y = x, y
        self.id = self.canvas.create_image(x, y)
        self.zoz = zoz
        self.faza = 0
        self.vel = min(zoz[0].width(), zoz[0].height()) / 2

    def dalsia_faza(self):
        self.faza = (self.faza + 1) % len(self.zoz)
        self.canvas.itemconfig(self.id, image=self.zoz[self.faza])

    def presun(self, x, y):
        self.canvas.move(self.id, x-self.x, y-self.y)
        self.x, self.y = x, y

    def vnutri(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2 <= self.vel**2