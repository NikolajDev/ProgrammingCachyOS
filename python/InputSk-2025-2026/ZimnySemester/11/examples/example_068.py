def pocet_samohlasok(slovo):
    return len(set(slovo) & set('aeiouy'))