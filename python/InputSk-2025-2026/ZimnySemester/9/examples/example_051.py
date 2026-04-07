import turtle

def nova(pos, heading):
    t = turtle.Turtle()
    #t.speed(0)
    #t.ht()
    t.pu()
    t.setpos(pos)
    t.seth(heading)
    t.pd()
    return t

def strom(n, d):
    zoznam = [nova([0, -300], 90)]
    for i in range(n):
        for j in range(len(zoznam)):
            t = zoznam[j]
            t.pensize(3 * n - 3 * i + 1)
            t.pencolor('maroon')
            t.fd(d)
            if i == n - 1:
                t.dot(20, 'green')
            else:
                zoznam.append(nova(t.pos(), t.heading() + 40))
                t.rt(50)
        d *= 0.6

    print('pocet korytnaciek =', len(zoznam))

# turtle.delay(0)
strom(7, 300)