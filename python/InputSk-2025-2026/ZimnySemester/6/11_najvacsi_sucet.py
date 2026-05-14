"""
Máme daný textový súbor, ktorý obsahuje len celé čísla, v kazdom riadku môže byť aj viac čísel oddelených medzerou. Napíš funkciu najvacsi_sucet(meno_suboru), ktorá vráti riadok súboru s naväčším súčtom čísel v riadku.

"""

def sucet_v_retazci(retazec):
    sucet = 0
    for val in retazec.split():
        sucet += int(val)
    return sucet

print(sucet_v_retazci('52 52 6'))

def najvacsi_sucet(meno_suboru):
    najvacsia_suma = 0
    najvacsi_riadok = ""
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru}") as file:
        lines = file.readlines()
    for num in lines:
        if sucet_v_retazci(num) > najvacsia_suma:
            najvacsi_riadok = num
            najvacsia_suma = sucet_v_retazci(num)
    return najvacsi_riadok