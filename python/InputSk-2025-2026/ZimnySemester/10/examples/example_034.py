def o_1_viac(tab):
    nova_tab = []
    for riadok in tab:
        novy_riadok = [0] * len(riadok)
        for i in range(len(riadok)):
            novy_riadok[i] = riadok[i] + 1
        nova_tab.append(novy_riadok)
    return nova_tab