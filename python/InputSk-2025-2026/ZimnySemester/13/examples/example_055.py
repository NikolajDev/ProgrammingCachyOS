class Korytnacka(Pero):
    def __init__(self):
        ...

    def lt(self, uhol):
        ...

    def rt(self, uhol):
        ...

    def fd(self, dlzka):
        ...

#---- test -------

t = Korytnacka()
for i in range(1, 200, 2):
    t.fd(i)
    t.lt(89)