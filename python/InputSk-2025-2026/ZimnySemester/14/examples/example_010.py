class Cas:

    ...

    def __add__(self, iny):
        return Cas(sekundy=self.sek + iny.sek)

    ...

c1 = Cas(10, 22, 30)
c2 = Cas(4, 55, 18)
print('sucet =', c1 + c2)