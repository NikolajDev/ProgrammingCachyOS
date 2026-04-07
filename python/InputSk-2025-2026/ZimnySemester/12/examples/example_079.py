class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        self.hod = hodiny
        self.min = minuty
        self.sek = sekundy

    def __str__(self):
        return f'{self.hod}:{self.min:02}:{self.sek:02}'

    def sucet(self, iny):
        return Cas(self.hod + iny.hod, self.min + iny.min, self.sek + iny.sek)

    def vacsi(self, iny):
        return (self.hod > iny.hod or
                self.hod == iny.hod and self.min > iny.min or
                self.hod == iny.hod and self.min == iny.min and self.sek > iny.sek)