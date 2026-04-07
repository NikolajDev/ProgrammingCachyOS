class Test1:
    def __getitem__(self, ix):
        if ix < 4:
            return (ix + 1) ** 2
        raise IndexError