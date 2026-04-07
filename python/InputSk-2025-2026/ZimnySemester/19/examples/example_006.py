def hladaj(hodnota, zoz):
    od, do = 0, len(zoz)
    while od <= do:
        stred = (od + do) // 2
        if zoz[stred] == hodnota:
            return True
        if zoz[stred] < hodnota:
            od = stred + 1
        else:
            do = stred - 1
    return False