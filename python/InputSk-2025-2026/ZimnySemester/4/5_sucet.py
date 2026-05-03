"""
odovzdaj Napš funkciu sucet(retazec, sustava=10), krorá dostáva znakový reťazec s celými číslami oddelenými znakom ','. Funkcia rozoberie tento reťazec (pomocou for-cyklu) na cifry, poskladá z nich číslo v zadanej číselnej sústave (napríklad pomocou int('1234', 5)) a všetky tieto čísla sčíta. Funkcia vráti (return) celé číslo. Napríklad

"""

def sucet(retazec, sustava=10):
    sum = 0
    help = ""
    for i in retazec:
        if i == ",":
            sum += int(help, sustava)
            help = ""
        else:
            help += i
    return sum+int(help, sustava)

print(sucet('11,247,3', 8))