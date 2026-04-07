class FarebnyBod(Bod):
    def __init__(self, x, y, farba='black'):
        Bod.__init__(self, x, y)             # inicializácia zo základnej triedy
        self.farba = farba
    ...