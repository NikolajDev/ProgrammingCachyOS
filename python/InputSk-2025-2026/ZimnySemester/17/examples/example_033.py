class AsocPole:
    def __init__(self):
        self.tab = [None] * 11
        self.num = 0

    def __contains__(self, kluc):
        bucket = self.tab[hash(kluc) % len(self.tab)]
        if bucket:
            for k, h in bucket:
                if k == kluc:
                    return True
        return False

    def __getitem__(self, kluc):
        bucket = self.tab[hash(kluc) % len(self.tab)]
        if bucket:
            for k, h in bucket:
                if k == kluc:
                    return h
        raise KeyError

    def __setitem__(self, kluc, hodnota):
        ix = hash(kluc) % len(self.tab)
        bucket = self.tab[ix]
        if bucket:
            for i, (k, h) in enumerate(bucket):
                if k == kluc:
                    bucket[i] = (kluc, hodnota)
                    return
        else:
            self.tab[ix] = bucket = []
        bucket.append((kluc, hodnota))
        self.num += 1
        if self.num > len(self.tab) * 0.9:
            self._resize(len(self.tab) * 2)

    def _resize(self, nova_dlzka):
        old_tab = self.tab
        self.tab = [None] * nova_dlzka
        self.num = 0
        for bucket in old_tab:
            if bucket is not None:
                for k, h in bucket:
                    self[k] = h

    def vypis(self):
        for i, bucket in enumerate(self.tab):
            if bucket:
                print(i, *bucket)