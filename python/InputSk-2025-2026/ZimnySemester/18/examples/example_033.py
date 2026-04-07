class Vizualizuj:
    def __init__(self, zoz):
        self.zoz = zoz

    def __getitem__(self, index):
        return self.zoz[index]

    def __len__(self):
        return len(self.zoz)

    def __setitem__(self, index, hodnota):
        self.zoz[index] = hodnota