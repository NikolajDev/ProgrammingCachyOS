def trojuholniky(n, a):
    if n > 0:
        for i in range(3):
            t.fd(a)
            t.lt(120)
            trojuholniky(n - 1, a / 2)

trojuholniky(4, 300)