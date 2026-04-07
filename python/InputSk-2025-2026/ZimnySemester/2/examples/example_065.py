def kombinacne_cislo(n, k):
    return faktorial(n) // (faktorial(n - k) * faktorial(k))