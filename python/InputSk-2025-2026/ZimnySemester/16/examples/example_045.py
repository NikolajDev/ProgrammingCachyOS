def mapuj(fun, postupnost):
    vysl = []
    for prvok in postupnost:
        vysl.append(fun(prvok))
    return vysl