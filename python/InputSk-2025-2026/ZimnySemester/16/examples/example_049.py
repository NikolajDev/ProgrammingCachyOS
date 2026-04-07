def filtruj(fun, postupnost):
    vysl = []
    for prvok in postupnost:
        if fun(prvok):
            vysl.append(prvok)
    return vysl