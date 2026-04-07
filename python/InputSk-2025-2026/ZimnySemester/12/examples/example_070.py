class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def __str__(self):
        return f'{self.hodiny}:{self.minuty:02}'

    def vypis(self):
        print('cas je', self)     # Python tu za nas urobil self.__str__()