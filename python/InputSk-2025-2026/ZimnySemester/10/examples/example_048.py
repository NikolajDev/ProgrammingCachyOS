def symetricka(matica):
    for i in range(1, len(matica)):
        for j in range(i):
            if matica[i][j] != matica[j][i]:
                return False
    return True