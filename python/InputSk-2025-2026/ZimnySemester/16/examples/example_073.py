class Fibonacci:
    def __iter__(self):
        self.f1, self.f2 = 0, 1
        return self

    def __next__(self):
        vysl = self.f1
        self.f1, self.f2 = self.f2, self.f1 + self.f2
##        if vysl > 100:
##            raise StopIteration
        return vysl