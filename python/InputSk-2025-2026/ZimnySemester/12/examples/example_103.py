class Kruh:
    canvas = None
    typ = 'kruh'

    def __init__(self, x, y, r, farba='red'):
        ...

class Obdlznik:
    canvas = None
    typ = 'obdlznik'

    def __init__(self, x, y, sirka, vyska, farba='red'):
        ...

class Skupina:
    ...
    def posun_typ(self, typ, dx=0, dy=0):
        for utvar in self.zoznam:
            if utvar.typ == typ:
                utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.zoznam:
            if utvar.typ == typ:
                utvar.prefarbi(farba)