class Cas:
    ...
    def kopia_a_pridaj(self, hodiny, minuty):
        novy = self.kopia()
        novy.pridaj(hodiny, minuty)
        return novy