class Vizualizuj:
    def __init__(self, zoz):
        self.zoz = zoz
        print('povodny zoznam =', zoz)

    def __getitem__(self, index):
        return self.zoz[index]

    def __len__(self):
        return len(self.zoz)

    def __setitem__(self, index, hodnota):
        self.zoz[index] = hodnota
        print(f'zoz[{index}] = {hodnota}')

def vymen(zoz, i, j):
    zoz[i], zoz[j] = zoz[j], zoz[i]

def min_sort(zoz):
    for i in range(len(zoz)-1):
        for j in range(i+1, len(zoz)):
            if zoz[i] > zoz[j]:
                vymen(zoz, i, j)

zz = [7, 16, 3, 9]
min_sort(Vizualizuj(zz))
print('výsledok =', zz)