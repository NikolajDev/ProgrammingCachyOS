def urob(n):
    m = {1}
    for i in range(n // 2):
        if i in m:
            if 2 * i + 1 <= n:
                m.add(2 * i + 1)
            if 3 * i + 1 <= n:
                m.add(3 * i + 1)
    return m