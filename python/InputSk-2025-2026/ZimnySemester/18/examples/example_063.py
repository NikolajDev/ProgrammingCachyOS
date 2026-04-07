def quick_sort(zoz):
    def quick(z, k):
        if z < k:
            # rozdelenie na dve casti
            index = z
            pivot = zoz[z]
            for i in range(z+1, k+1):
                if zoz[i] < pivot:
                    index += 1
                    vymen(zoz, index, i)
            vymen(zoz, index, z)
            # v index je teraz pozicia pivota
            print(*zoz)                         # <== vypis
            quick(z, index-1)
            quick(index+1, k)
    print(*zoz)                                 # <== vypis
    quick(0, len(zoz)-1)

z = [32, 12, 66, 19, 75, 29, 50]
quick_sort(z)