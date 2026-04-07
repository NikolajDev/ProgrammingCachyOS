def slovo(veta):
    for i in range(len(veta)):
        if not je_pismeno(veta[i]):
            return veta[:i]
    return veta