class Skupina:
    ...

    def prefarbi(self, farba):
        for utvar in self.zoznam:
            utvar.prefarbi(farba)

    def posun(self, dx=0, dy=0):
        for utvar in self.zoznam:
            utvar.posun(dx, dy)