class FarebnyBod(Bod):
    def __init__(self, x, y, farba='black'):
        self.__init__(x, y)                   # !!! chybné volanie !!!
        self.farba = farba
    ...