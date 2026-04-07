class AsocPole:
    def __init__(self, kapacita=1000):
        self.tab = [None] * kapacita

    def __contains__(self, kluc):
        return 0 <= kluc < len(self.tab) and self.tab[kluc] is not None

    def __getitem__(self, kluc):
        if kluc < 0 or kluc >= len(self.tab) or self.tab[kluc] is None:
            raise KeyError
        return self.tab[kluc]

    def __setitem__(self, kluc, hodnota):
        if kluc < 0 or kluc >= len(self.tab):
            raise KeyError
        self.tab[kluc] = hodnota