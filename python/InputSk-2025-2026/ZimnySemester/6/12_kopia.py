"""
odovzdaj Napíš funkciu kopia(meno_suboru1, meno_suboru2, od=None, do=None), ktorá urobí kópiu riadkov z uzavretého intervalu <od, do> (riadky číslujeme od 0) súboru meno_suboru1 do nového súboru meno_suboru2. Ak má parameter od hodnotu None, znamená to, že robíme kópiu už od začiatku a podobne, ak má parameter do hodnotu None, znamená to, že robíme kópiu až do konca súboru.

"""

def kopia(meno_suboru1, meno_suboru2, od=None, do=None):
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru1}") as file:
        lines = file.readlines()
    zaciatok = 0
    koniec = len(lines)
    if od is not None:
        zaciatok = od
    if do is not None:
        koniec = do
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru2}", 'w') as file:
        file.writelines(lines[zaciatok:koniec+1])


kopia("najdlhsi_riadok.txt", 'copyright.txt', 0, 3)
