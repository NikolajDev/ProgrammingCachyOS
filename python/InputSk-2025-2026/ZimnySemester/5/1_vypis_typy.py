"""
Napíš funkciu vypis_typy(zoznam), ktorá vypíše všetky prvky zoznamu a ku každému vypíše informáciu o jeho type: ak je to int alebo float, tak vypíše 'číslo'; ak je to str, tak vypíše 'reťazec'; inak všetky ostatné typy vypíše ako 'iný typ'. Napríklad:

vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])
    12 - číslo
    x - reťazec
    None - iný typ
    3.14 - číslo
    [] - iný typ
    range(0, 5) - iný typ
    123 - reťazec
Môžeš využiť takýto test: if type(prvok) == str: ....

"""


def vypis_typy(zoznam):
    for prvok in zoznam:
        if type(prvok) == int or type(prvok) == float:
            print(f"{prvok} - číslo")
        elif type(prvok) == str:
            print(f"{prvok} - reťazec")
        else:
            print(f"{prvok} - iný typ")

vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])