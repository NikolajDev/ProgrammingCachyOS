def zoznam_bez_retazcov(zoznam):
    novy = []
    for prvok in zoznam:
        if type(prvok) != str:
            novy.append(prvok)
    return novy