def eratostenovo_sito(n):
    mnozina = set(range(2, n + 1))
    for i in range(n):
        if i in mnozina:
            mnozina -= set(range(i + i, n + 1, i))
    return mnozina