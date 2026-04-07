def poly(pocet, dlzka, uhol):
    if pocet <= 0:
        pass          # nič nerob len skonči
    else:
        t.fd(dlzka)
        t.lt(uhol)
        poly(pocet - 1, dlzka, uhol)