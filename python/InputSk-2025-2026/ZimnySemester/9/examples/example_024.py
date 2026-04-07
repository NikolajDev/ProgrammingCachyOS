def poly(pocet, dlzka, uhol):
    if pocet > 0:
        t.fd(dlzka)
        t.lt(uhol)
        poly(pocet - 1, dlzka, uhol)