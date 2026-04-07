def pocet_vyskytov(podretazec, retazec):
    '''funkcia vráti počet výskytov podreťazca v reťazci

    prvý parameter podretazec - ľubovoľný neprázdny reťazec, o ktorom sa
                                bude zisťovať počet výskytov
    druhý parameter retazec - reťazec, v ktorom sa hľadajú výskyty

    ak je prvý parameter podretazec prázdny reťazec, funkcia vráti len(retazec)
    '''
    pocet = 0
    for ix in range(len(retazec)):
        if retazec[ix:ix + len(podretazec)] == podretazec:
            pocet += 1
    return pocet