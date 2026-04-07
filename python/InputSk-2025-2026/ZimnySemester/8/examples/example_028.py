import turtle

def stvorec(tu, velkost):
    for i in range(4):
        tu.fd(velkost)
        tu.rt(90)

t = turtle.Turtle()
stvorec(t, 100)
turtle.done()