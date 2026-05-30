"""
Napíš funkciu najdlhsi_riadok(meno_suboru), ktorá pre 
zadaný súbor vráti najdlhší riadok (aj s koncovým '\n').

"""


def najdlhsi_riadok(meno_suboru):
    riadky = []
    najdlhsi = ""
    with open(meno_suboru) as file:
        riadky = file.readlines()
    for riadok in riadky:
        if len(riadok) > len(najdlhsi):
            najdlhsi = riadok
    return najdlhsi


if __name__ == "__main__":
    print(najdlhsi_riadok("najdlhsi_riadok.txt"))
