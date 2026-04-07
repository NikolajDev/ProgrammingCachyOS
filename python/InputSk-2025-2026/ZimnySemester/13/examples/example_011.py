class Bod:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'Bod({self.x}, {self.y})'

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

bod = Bod(100, 50)
bod.posun(-10, 40)
print('bod =', bod)