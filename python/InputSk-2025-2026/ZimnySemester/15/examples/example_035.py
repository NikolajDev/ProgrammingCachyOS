def strom(n, d):

# prvá časť
    t.fd(d)
    if n <= 0:
        t.bk(d)         # triviálny prípad
    else:
        t.lt(40)
        strom(n - 1, d * 0.7)

# druhá časť
        t.rt(75)
        strom(n - 1, d * 0.6)

# tretia časť
        t.lt(35)
        t.bk(d)