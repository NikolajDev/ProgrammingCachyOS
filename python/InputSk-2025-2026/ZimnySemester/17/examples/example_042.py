class AsocPole:
    def __init__(self):
        self.tab = []

    def __contains__(self, kluc):
        for k, h in self.tab:
            if k == kluc:
                return True
        return False

    def __getitem__(self, kluc):
        for k, h in self.tab:
            if k == kluc:
                return h
        raise KeyError

    def __setitem__(self, kluc, hodnota):
        for i, (k, h) in enumerate(self.tab):
            if k == kluc:
                self.tab[i] = (kluc, hodnota)
                return
        self.tab.append((kluc, hodnota))