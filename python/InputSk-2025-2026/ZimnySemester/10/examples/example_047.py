def symetricka(matica):
    vysl = True
    for i in range(len(matica)):
        for j in range(len(matica[i])):
            if matica[i][j] != matica[j][i]:
                vysl = False
                break                     # vyskočí z cyklu
    return vysl