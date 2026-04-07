class Student:

    def __init__(self, meno, priezvisko, hoby=''):
        self.meno = meno
        self.priezvisko = priezvisko
        self.hoby = hoby

    def vypis(self):
        print('volam sa', self.meno, self. priezvisko)

    def nastav_hoby(self, text):
        self.hoby = text
        print(self.meno, self. priezvisko, 'ma hoby', self.hoby)