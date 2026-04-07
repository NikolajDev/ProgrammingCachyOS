def stvorec(a):
    if a > 100:
        pass          # nič nerob len skonči
    else:
        poly(4, a, 90)
        stvorec(a + 5)

def stvorec1(a):
    if a > 100:
        t.lt(180)       # a skonči
    else:
        poly(4, a, 90)
        stvorec1(a + 5)
        poly(4, a, 90)