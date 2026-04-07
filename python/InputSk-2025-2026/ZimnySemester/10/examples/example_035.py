def o_1_viac(tab):
    nova_tab = []
    for riadok in tab:
        novy_riadok = list(riadok)          # kópia pôvodného riadka
        for i in range(len(novy_riadok)):
            novy_riadok[i] += 1
        nova_tab.append(novy_riadok)
    return nova_tab