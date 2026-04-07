with open('subor3.txt', 'r') as t:
    cely = t.read()                        # zapamätá si pôvodný obsah
with open('subor3.txt', 'w') as t:         # vymaže všetko
    t.write(cely)                          # vráti tam pôvodný obsah
    t.write('pridany riadok na koniec\na este jeden\n')