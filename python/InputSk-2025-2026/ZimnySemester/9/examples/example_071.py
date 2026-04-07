def mocnina(n, k):
    if k == 0:
        return 1
    return n * mocnina(n, k - 1)

print(mocnina(2, 900) == 2 ** 900)