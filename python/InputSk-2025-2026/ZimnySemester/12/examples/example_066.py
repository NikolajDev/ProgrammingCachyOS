class Cas:
    ...
    def pridaj(self, hodiny, minuty):
        self.hodiny += hodiny + (self.minuty + minuty) // 60
        self.minuty = (self.minuty + minuty) % 60