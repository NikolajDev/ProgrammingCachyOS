def test(i):
    if i <= 1:
        return i == 1
    return i % 2 == 1 and test(i // 2) or i % 3 == 1 and test(i // 3)