class Kruh:
    ...
    def __str__(self):
        return f'Kruh({self.x},{self.y},{self.r},{self.farba!r})'

class Obdlznik:
    ...
    def __str__(self):
        return f'Obdlznik({self.x},{self.y},{self.sirka},{self.vyska},{self.farba!r})'

...
for utvar in sk.zoznam:
    print(utvar)