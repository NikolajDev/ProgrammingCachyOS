import turtle

def strom(n):
    if n == 0:
        t.fd(30)        # triviálny prípad
        t.bk(30)
    else:
        t.fd(30)
        t.lt(40)        # natoč sa na kreslenie ľavého podstromu
        strom(n - 1)    # nakresli ľavý podstrom (n-1). úrovne
        t.rt(80)        # natoč sa na kreslenie pravého podstromu
        strom(n - 1)    # nakresli pravý podstrom (n-1). úrovne
        t.lt(40)        # natoč sa do pôvodného smeru
        t.bk(30)        # vráť sa na pôvodné miesto

t = turtle.Turtle()
t.lt(90)
strom(4)