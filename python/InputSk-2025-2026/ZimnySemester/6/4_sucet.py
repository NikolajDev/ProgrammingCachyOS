"""
Napíš funkciu sucet(retazec), ktorá dostáva znakový reťazec s niekoľkými celými číslami oddelenými znakom '+'. Funkcia vráti (nič nevypisuje) celé číslo, ktoré je súčtom všetkých čísel v reťazci. Vstupný reťazec obsahuje aspoň jedno číslo a keď ich je viac, sú oddelené znakom '+'. Medzery medzi číslami a '+' sa ignoruju. Funkcia vypočíta súčet. Napríklad:

x = sucet('12+9')
x
    21
sucet('1+2 + 3+4')
    10
sucet('1234')
    1234

"""

def sucet(retazec):
    idx = 0
    num = ""
    result = 0
    while idx < len(retazec):
        if retazec[idx] == '+':
            result += int(num)
            num = ""
        else:
            num += retazec[idx]
        idx += 1
    return result + int(num)

print(sucet('1234'))