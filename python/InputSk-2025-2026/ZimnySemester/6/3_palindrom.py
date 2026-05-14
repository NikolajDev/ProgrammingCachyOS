"""
odovzdaj Napíš funkciu je_palindrom(reťazec), ktorá zistí (vráti True alebo False), či je zadaný reťazec palindróm. Funkcia ignoruje medzery a nerozlišuje medzi malými a veľkými písmenami. Napríklad:

je_palindrom('Python')
    False
je_palindrom('tahat')
    True
je_palindrom('Jelenovi Pivo Nelej')
    True
"""

def je_palindrom(retazec):
    return retazec.lower().replace(" ", "") == retazec.lower().replace(" ", "")[::-1]

print(je_palindrom("Python"))
print(je_palindrom('Jelenovi Pivo Nelej'))