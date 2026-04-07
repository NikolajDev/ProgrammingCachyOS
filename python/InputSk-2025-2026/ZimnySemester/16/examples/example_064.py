class Test:
    def __init__(self, od, do):
        self.od, self.do = od, do

    def __iter__(self):
        return TestIterator(self.od, self.do)

class TestIterator:
    def __init__(self, od, do):
        self.x, self.do = od, do

    def __next__(self):
        if self.x > self.do:
            raise StopIteration
        self.x += 1
        return self.x - 1