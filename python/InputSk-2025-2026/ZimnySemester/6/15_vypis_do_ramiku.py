"""
odovzdaj Napíš funkciu vypis_do_ramiku(meno_suboru1, meno_suboru2=None), ktorá zadaný súbor vypíše do meno_suboru2 s rámikom z hviezdičiek, pričom má tento rámik šírku podľa dĺžky najdlhšieho riadka. Ak má parameter meno_suboru2 hodnotu None, výpis bude do konzoly Napríklad, pre textový súbor:

"""

def vypis_do_ramiku(meno_suboru1, meno_suboru2=None):
    # Otvorenie vstupného súboru a načítanie riadkov
    # Cestu si uprav podľa potreby, v zadaní sa zvyčajne predpokladá len meno_suboru1
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru1}", 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    
    # Zistenie dĺžky najdlhšieho riadka
    if not lines:
        max_length = 0
    else:
        max_length = max(len(line) for line in lines)

    # Vytvorenie vrchného a spodného rámika
    horny_spodny_ramik = "*" * (max_length + 4)
    
    # Príprava výsledného textu
    vysledok = [horny_spodny_ramik]
    for line in lines:
        # Každý riadok doplníme medzerami tak, aby lícoval s najdlhším
        vysledok.append(f"* {line.ljust(max_length)} *")
    vysledok.append(horny_spodny_ramik)

    # Spojenie do jedného textového bloku
    finalny_text = "\n".join(vysledok)

    # Logika pre výpis (konzola vs súbor)
    if meno_suboru2 is None:
        print(finalny_text)
    else:
        with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru2}", 'w', encoding='utf-8') as out_file:
            out_file.write(finalny_text)

# Test volania
vypis_do_ramiku("najdlhsi_riadok.txt")