import turtle

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

t = turtle.Turtle()
stvorec(100)
t.pu()
t.lt(70)
t.fd(80)
t.pd()
stvorec(50)
turtle.done()