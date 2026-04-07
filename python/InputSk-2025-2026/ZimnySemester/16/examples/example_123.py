def cele_cisla():
    i = 1
    while True:
        yield i
        i = i + 1

def mocniny():
    for i in cele_cisla():
        yield i * i

def zisti(n, post):
    post = iter(post)
    vysl = []
    try:
        for i in range(n):
            vysl.append(next(post))
    except StopIteration:
        pass
    return vysl

print(zisti(5, mocniny()))