def bubble_sort(p):
    b = True
    while b:
        b = False
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                b = True