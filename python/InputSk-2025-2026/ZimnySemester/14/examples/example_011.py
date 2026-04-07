class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        self.sek = abs(3600 * hodiny + 60 * minuty + sekundy)

    def __str__(self):
        return f'{self.sek // 3600}:{self.sek // 60 % 60:02}:{self.sek % 60:02}'

    def __add__(self, iny):
        return Cas(sekundy=self.sek + iny.sek)

    def __sub__(self, iny):
        return Cas(sekundy=self.sek - iny.sek)

    def __gt__(self, iny):
        return self.sek > iny.sek

    def __eq__(self, iny):
        return self.sek == iny.sek