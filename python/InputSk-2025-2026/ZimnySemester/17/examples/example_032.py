def __setitem__(self, kluc, hodnota):
    ...
    if self.num > len(self.tab) * 0.9:
        self._resize(len(self.tab) * 2)