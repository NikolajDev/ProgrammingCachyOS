turtle.delay(0)
zoz = []
moja = (MojaTurtle, MojaTurtle1, MojaTurtle2)
for i in range(100):
    t = random.choice(moja)()   # všimnite si zátvorky na konci
    t.ht()
    t.speed(0)
    t.pu()
    t.setpos(random.randint(-300, 250), random.randint(-250, 250))
    t.pd()
    zoz.append(t)

for t in zoz:
    t.domcek(50)