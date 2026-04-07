def pocet(tab, hodnota):
    return sum(prvok == hodnota for riadok in tab for prvok in riadok)