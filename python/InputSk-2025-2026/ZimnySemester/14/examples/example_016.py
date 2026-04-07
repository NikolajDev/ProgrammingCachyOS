class Zlomok:

    def __init__(self, citatel=0, menovatel=1):

        def nsd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if menovatel == 0:
            menovatel = 1
        delitel = nsd(citatel, menovatel)
        self.cit = citatel // delitel
        self.men = menovatel // delitel

    def __str__(self):
        return f'{self.cit}/{self.men}'

    __repr__ = __str__

    def __add__(self, iny):
        if isinstance(iny, int):
            c, m = iny, 1
        else:
            c, m = iny.cit, iny.men
        return Zlomok(self.cit * m + self.men * c, self.men * m)

    __radd__ = __add__

    def __sub__(self, iny):
        if isinstance(iny, int):
            c, m = iny, 1
        else:
            c, m = iny.cit, iny.men
        return Zlomok(self.cit * m - self.men * c, self.men * m)

    def __rsub__(self, iny):
        if isinstance(iny, int):
            c, m = iny, 1
        else:
            c, m = iny.cit, iny.men
        return Zlomok(self.men * c - self.cit * m, self.men * m)

    def __mul__(self, iny):
        if isinstance(iny, int):
            c, m = iny, 1
        else:
            c, m = iny.cit, iny.men
        return Zlomok(self.cit * c, self.men * m)

    __rmul__ = __mul__

    def __abs__(self):
        return Zlomok(abs(self.cit), self.men)

    def __int__(self):
        return self.cit // self.men

    def __float__(self):
        return self.cit / self.men

    def __lt__(self, iny):
        return self.cit * iny.men < self.men * iny.cit

    def __eq__(self, iny):
        return self.men == iny.men and self.cit == iny.cit
        # alebo: return (self.cit, self.men) == (iny.cit, iny.men)