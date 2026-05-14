"""
Napíš funkciu najdlhsi_riadok(meno_suboru), ktorá pre 
zadaný súbor vráti najdlhší riadok (aj s koncovým '\n').

"""


def najdlhsi_riadok(meno_suboru):
    riadky = []
    najdlhsi = ""
    with open(f"./python/InputSk-2025-2026/ZimnySemester/6/{meno_suboru}") as file:
        riadky = file.readlines()
    for riadok in riadky:
        if len(riadok) > len(najdlhsi):
            najdlhsi = riadok
    return najdlhsi


print(najdlhsi_riadok("najdlhsi_riadok.txt"))
