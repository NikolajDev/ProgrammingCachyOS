class Cas:
    ...
    def kopia_a_pridaj(self, hodiny, minuty):
        novy = Cas(self.hodiny, self.minuty)
        novy.pridaj(hodiny, minuty)
        return novy