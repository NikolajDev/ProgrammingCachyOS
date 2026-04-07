def test(i):
    if i == 0:
        return False
    if i == 1:
        return True
    if i % 2 == 1 and test(i // 2):
        return True
    if i % 3 == 1 and test(i // 3):
        return True
    return False