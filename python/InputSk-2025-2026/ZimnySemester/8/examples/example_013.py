import turtle
import random

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def trojuholnik(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(3):
        t.fd(dlzka)
        t.rt(120)
    t.end_fill()

def dom(d):
    t.pu()
    stvorec(d)
    t.lt(60)
    trojuholnik(d)
    t.rt(60)

def posun():
    t.pu()
    t.setpos(random.randint(-200, 200), random.randint(-100, 100))
    t.seth(random.randint(-30, 30))
    t.pd()

turtle.delay(0)
t = turtle.Turtle()
for i in range(20):
    posun()
    dom(random.randint(10, 40))
turtle.done()