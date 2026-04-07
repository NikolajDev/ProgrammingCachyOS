def pocet_samohlasok(slovo):
    vysl = 0
    for znak in 'aeiouy':
        if znak in slovo:
            vysl += 1
    return vysl