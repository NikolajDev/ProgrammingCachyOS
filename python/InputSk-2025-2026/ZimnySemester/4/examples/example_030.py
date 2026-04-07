def ma_delitela(cislo):
    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            return True
    return False