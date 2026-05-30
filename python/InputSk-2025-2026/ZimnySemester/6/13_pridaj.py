"""

Napíš funkciu pridaj(meno_suboru, text), ktorá do textového súboru pridá na začiatok nový riadok so zadaným textom. Napríklad, ak súbor obsahoval riadky:

prvý riadok
druhý riadok
potom volania:

pridaj('subor.txt', 'nový riadok\n')
zmenia tento súbor:

nový riadok
predposledný
posledný riadok

"""

def pridaj(meno_suboru, text):
    with open(meno_suboru) as file:
        text_povodny = file.read()
    
    with open(meno_suboru, 'w') as file:
        file.write(text + text_povodny)
    
if __name__ == "__main__":
    pridaj('subor.txt', 'nový riadok\n')