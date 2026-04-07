import turtle

def ckrivka(n, s):
    if n == 0:
        t.fd(s)
    else:
        ckrivka(n - 1, s)
        t.lt(90)
        ckrivka(n - 1, s)
        t.rt(90)

turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.ht()
ckrivka(9, 4)    # skúste aj: ckrivka(13, 2)