class FarebnyBod(Bod):
    def __init__(self, x, y, farba='black'):
        self.x = x
        self.y = y
        self.farba = farba

    def zmen_farbu(self, farba):
        self.farba = farba

fbod = FarebnyBod(200, 50, 'green')
fbod.posun(dy=50)
print('fbod =', fbod)