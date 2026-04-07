class AsocPole:
    def __init__(self):
        self.tab = [None] * 11
        self.num = 0

    def _find(self, kluc):
        '''vráti dvojicu
            (True, index) - ak nájde kľúč
            (False, prvý voľný) - ak nenájde kľúč
        '''
        ix = hash(kluc) % len(self.tab)
        av = None                # prvý voľný
        while True:
            prvok = self.tab[ix]
            if prvok is None:
                if av is None:
                    av = ix
                return False, av
            if prvok[0] == kluc:
                return True, ix
            ix = (ix + 1) % len(self.tab)

    def __contains__(self, kluc):
        return self._find(kluc)[0]

    def __getitem__(self, kluc):
        nasiel, ix = self._find(kluc)
        if nasiel:
            return self.tab[ix][1]
        raise KeyError

    def __setitem__(self, kluc, hodnota):
        nasiel, ix = self._find(kluc)
        if nasiel:
            self.tab[ix] = (kluc, hodnota)
            return
        self.tab[ix] = (kluc, hodnota)
        self.num += 1
        if self.num > len(self.tab) * 0.66:
            self._resize(len(self.tab) * 2)

    def _resize(self, nova_dlzka):
        old_tab = self.tab
        self.tab = [None] * nova_dlzka
        self.num = 0
        for prvok in old_tab:
            if prvok is not None:
                k, h = prvok
                self[k] = h

    def vypis(self):
        for i, prvok in enumerate(self.tab):
            if prvok:
                print(i, prvok)