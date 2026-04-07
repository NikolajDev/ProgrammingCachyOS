class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        cas = abs(3600 * hodiny + 60 * minuty + sekundy)
        self.hod = cas // 3600
        self.min = cas // 60 % 60
        self.sek = cas % 60

    def __str__(self):
        return f'{self.hod}:{self.min:02}:{self.sek:02}'

    def sucet(self, iny):
        return Cas(self.hod + iny.hod, self.min + iny.min, self.sek + iny.sek)

    def rozdiel(self, iny):
        return Cas(sekundy = self.pocet_sekund() - iny.pocet_sekund())

    def pocet_sekund(self):
        return 3600 * self.hod + 60 * self.min + self.sek

    def vacsi(self, iny):
        return self.pocet_sekund() > iny.pocet_sekund()

cas1 = Cas(10, 22, 30)
cas2 = Cas(9, 58, 45)
print('cas1 =', cas1)
print('cas2 =', cas2)
print('sucet =', cas1.sucet(cas2))
print('cas1 > cas2 =', cas1.vacsi(cas2))
print('cas2 > cas1 =', cas2.vacsi(cas1))
print('cas1 - cas2 =', cas1.rozdiel(cas2))
print('cas2 - cas1 =', cas2.rozdiel(cas1))