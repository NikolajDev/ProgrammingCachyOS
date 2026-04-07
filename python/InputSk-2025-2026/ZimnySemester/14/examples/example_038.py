try:
    with open('x.txt') as subor:
        cislo = int(subor.readline())
except FileNotFoundError:
    print('*** neexistujuci subor ***')
    cislo = 0
except (ValueError, TypeError):
    print('*** prvy riadok suboru neobsahuje cele cislo ***')
    cislo = 10