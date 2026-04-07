class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f'cas je {self.hodiny}:{self.minuty:02}')

    def str(self):
        return f'{self.hodiny}:{self.minuty:02}'