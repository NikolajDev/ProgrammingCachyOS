class UcetHeslo:
    def __init__(self, meno, heslo, suma=0):
        self.meno, self.heslo, self.suma = meno, heslo, suma

    def __str__(self):
        return f'ucet {self.meno} -> {self.suma} euro'

    def vklad(self, suma):
        if self.heslo == input(f'heslo pre {self.meno}? '):
            self.suma += suma
        else:
            print('chybne heslo')

    def vyber(self, suma):
        if self.heslo == input(f'heslo pre {self.meno}? '):
            if suma <= 0:
                return 0
            suma = min(self.suma, suma)
            self.suma -= suma
            return suma
        else:
            print('chybne heslo')

#---- test ----

mbank = UcetHeslo('mbank', 'heslo1', 100)
csob = UcetHeslo('csob', 'heslo2', 30)
print('*** stav uctov:', mbank, csob, sep='\n')
mbank.vklad(csob.vyber(55))
print('*** stav uctov:', mbank, csob, sep='\n')