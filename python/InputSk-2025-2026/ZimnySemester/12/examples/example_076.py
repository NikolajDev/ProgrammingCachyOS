class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def __str__(self):
        return f'{self.hodiny}:{self.minuty:02}'

    def vypis(self):
        print('cas je', self)

    def kopia(self):
        return Cas(self.hodiny, self.minuty)

    def pridaj(self, hodiny, minuty):
        self.hodiny += hodiny + (self.minuty+minuty) // 60
        self.minuty = (self.minuty+minuty) % 60