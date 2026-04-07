import random

def pridaj():
    for i in range(20):
        if random.randrange(2):
            sk.pridaj(Kruh(random.randint(50, 350), random.randint(50, 350),
                           random.randint(10, 25)))
        else:
            sk.pridaj(Obdlznik(random.randint(50, 350), random.randint(50, 350),
                               random.randint(10, 50), random.randint(10, 50)))

def zmen1():
    sk.zmen_farbu(f'#{random.randrange(256**3):06x}')
    sk.posun(2, 5)

def zmen2():
    sk.zmen_farbu('yellow', Kruh)
    sk.posun(-10, -25, Obdlznik)

tkinter.Button(text='pridaj', command=pridaj).pack()
tkinter.Button(text='zmen1', command=zmen1).pack()
tkinter.Button(text='zmen2', command=zmen2).pack()

sk = Skupina()