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
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru}") as file:
        text_povodny = file.read()
    
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru}", 'w') as file:
        file.writable(text + text_povodny)
    
pridaj('subor.txt', 'nový riadok\n')