def podiel(p1, p2):
    assert isinstance(p1, int), 'prvy parameter nie je cele cislo'
    assert isinstance(p2, int), 'druhy parameter nie je cele cislo'
    assert p2 != 0, 'neda sa delit nulou'
    return p1 // p2