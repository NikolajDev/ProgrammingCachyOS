class AsocPole:
    def __init__(self, kapacita=50):
        self.tab = [[] for i in range(kapacita)]

    def __contains__(self, kluc):
        bucket = self.tab[kluc % len(self.tab)]
        for k, h in bucket:
            if k == kluc:
                return True
        return False

    def __getitem__(self, kluc):
        bucket = self.tab[kluc % len(self.tab)]
        for k, h in bucket:
            if k == kluc:
                return h
        raise KeyError

    def __setitem__(self, kluc, hodnota):
        bucket = self.tab[kluc % len(self.tab)]
        for i, (k, h) in enumerate(bucket):
            if k == kluc:
                bucket[i] = (kluc, hodnota)
                return
        bucket.append((kluc, hodnota))