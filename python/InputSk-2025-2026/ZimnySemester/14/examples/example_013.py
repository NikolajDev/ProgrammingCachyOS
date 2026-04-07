class Zlomok:
    def __init__(self, citatel=0, menovatel=1):
        self.cit = citatel
        self.men = menovatel

    def __str__(self):
        return f'{self.cit}/{self.men}'

    def __int__(self):
        return self.cit // self.men

    def __float__(self):
        return self.cit / self.men