def quick_sort(zoz):
    def quick(z, k):
        if z < k:
            # rozdelenie na dve časti
            index = z
            pivot = zoz[index]
            for i in range(z+1, k+1):
                if zoz[i] < pivot:
                    index += 1
                    vymen(zoz, index, i)
            vymen(zoz, index, z)
            # v index je teraz pozícia pivota
            quick(z, index-1)
            quick(index+1, k)

    quick(0, len(zoz)-1)