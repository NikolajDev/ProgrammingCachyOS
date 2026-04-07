import turtle

def posun(k, pos):     # pos je pozícia v tvare (x, y)
    k.pu()
    k.setpos(pos)
    k.pd()

def stred(k1, k2):
    x = (k1.xcor() + k2.xcor()) / 2
    y = (k1.ycor() + k2.ycor()) / 2
    return (x, y)

turtle.delay(0)
t1 = turtle.Turtle()
posun(t1, (-150, 30))
t2 = turtle.Turtle()
posun(t2, (250, 0))
t3 = turtle.Turtle()
posun(t3, stred(t1, t2))
t3.pencolor('red')

while True:
    t1.fd(4)
    t1.rt(3)
    t2.fd(3)
    t2.lt(2)
    t3.setpos(stred(t1, t2))
# turtle.done()