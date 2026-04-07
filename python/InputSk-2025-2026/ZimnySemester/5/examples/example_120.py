def zoznam_bez_retazcov(zoznam):
    kopia = zoznam
    for prvok in zoznam:
        if type(prvok) == str:
            kopia.remove(prvok)
    return kopia