def meno(r):
    ix = 0
    while ix < len(r) and r[ix] != ' ':     # najde medzeru
        ix += 1
    return r[ix + 1:] + ' ' + r[:ix]