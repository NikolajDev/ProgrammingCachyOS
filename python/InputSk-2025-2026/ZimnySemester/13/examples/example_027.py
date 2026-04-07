class Skupina:
    def __init__(self):
        self._zoznam = []

    def pridaj(self, utvar):
        self._zoznam.append(utvar)

##    def posun(self, dx, dy):
##        for utvar in self._zoznam:
##            utvar.posun(dx, dy)

    def posun(self, dx, dy, typ=Utvar):
        for utvar in self._zoznam:
            if isinstance(utvar, typ):
                utvar.posun(dx, dy)

##    def zmen_farbu(self, farba):
##        for utvar in self._zoznam:
##            utvar.zmen_farbu(farba)

    def zmen_farbu(self, farba, typ=Utvar):
        for utvar in self._zoznam:
            if isinstance(utvar, typ):
                utvar.zmen_farbu(farba)