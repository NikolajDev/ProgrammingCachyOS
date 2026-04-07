class Skupina:
    def __init__(self):
        self._zoznam = []

    def pridaj(self, utvar):
        self._zoznam.append(utvar)

    def posun(self, dx, dy):
        for utvar in self._zoznam:
            utvar.posun(dx, dy)

    def posun_typ(self, dx, dy, typ):
        for utvar in self._zoznam:
            if isinstance(utvar, typ):
                utvar.posun(dx, dy)

    def zmen_farbu(self, farba):
        for utvar in self._zoznam:
            utvar.zmen_farbu(farba)

    def zmen_farbu_typ(self, farba, typ):
        for utvar in self._zoznam:
            if isinstance(utvar, typ):
                utvar.zmen_farbu(farba)