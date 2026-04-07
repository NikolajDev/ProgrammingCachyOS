def podiel(p1, p2):
    if not isinstance(p1, int):
        raise MojaChyba('prvy parameter nie je cele cislo')
    if not isinstance(p2, int):
        raise MojaChyba('druhy parameter nie je cele cislo')
    if p2 == 0:
        raise MojaChyba('neda sa delit nulou')
    return p1 // p2