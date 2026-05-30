"""
odovzdaj Napíš funkciu rozsekaj(text, sirka), ktorá vráti zadaný text ako viacriadkový reťazec, pričom každý (možno okrem posledného) má presne sirka znakov. Napríklad:

ret = rozsekaj('Anicka dusicka, kde si bola', 10)
ret
    'Anicka dus\nicka, kde \nsi bola'
print(ret)
    Anicka dus
    icka, kde
    si bola
    
"""

def rozsekaj(text, sirka):
    len = 1
    result = ""
    for letter in text:
        if len == sirka:
            result += f"{letter}\n"
            len = 1
        else:
            result += letter
            len += 1
    return result

if __name__ == "__main__":
    print(rozsekaj('Anicka dusicka, kde si bola', 10))