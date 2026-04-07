class ChybnaTransakcia(Exception): pass

class UcetHeslo:
    def __init__(self, meno, heslo, suma=0):
        self.meno, self.heslo, self.suma = meno, heslo, suma

    def __str__(self):
        return f'ucet {self.meno} -> {self.suma} euro'

    def kontrola(self):
        if self.heslo and self.heslo != input(f'heslo pre {self.meno}? '):
            raise ChybnaTransakcia('chybne heslo pre pristup k uctu ' + self.meno)

    def vklad(self, suma):
        self.kontrola()
        try:
            if suma <= 0:
                raise TypeError
            self.suma += suma
        except TypeError:
            raise ChybnaTransakcia('chybne zadana suma pre vklad na ucet ' + self.meno)

    def vyber(self, suma):
        self.kontrola()
        try:
            if suma <= 0:
                raise TypeError
            suma = min(self.suma, suma)
            self.suma -= suma
            return suma
        except TypeError:
            raise ChybnaTransakcia('chybne zadana suma pre vyber z uctu ' + self.meno)

def prevod(ucet1, ucet2, suma):
    '''prevedie sumu z ucet1 na ucet2'''
    suma = ucet1.vyber(suma)
    try:
        ucet2.vklad(suma)
    except ChybnaTransakcia:
        ucet1.suma += suma   # vrati vybratu sumu na ucet1
        raise

#---- test ----

mbank = UcetHeslo('mbank', 'heslo1', 100)
csob = UcetHeslo('csob', 'heslo2', 30)
print('*** stav uctov:', mbank, csob, sep='\n')
prevod(csob, mbank, 55)
print('*** stav uctov:', mbank, csob, sep='\n')