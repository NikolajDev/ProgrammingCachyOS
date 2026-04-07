zoznam = ['red', 'blue', 'gold', 'green']

def strom(d):
    t.fd(d)
    if d > 10:
        t.lt(40)
        strom(d * 0.7)
        t.rt(75)
        strom(d * 0.6)
        t.lt(35)
    t.bk(d)

t.lt(90)
t.pu()
t.fd(-200)
t.pd()
strom(100)