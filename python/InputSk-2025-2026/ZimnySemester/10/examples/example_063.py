import random

def zmen():
    for i in range(n):
        t[i] = t[i][:i + 1]               # každý i-ty riadok sa skráti na i+1 prvkov
    kresli(t)

canvas = tkinter.Canvas()
canvas.pack()
tkinter.Button(text='Zmeň', command=zmen).pack()

n = 11
t = vyrob(n, n)                           # tabuľka n x n samých 0
for riadok in t:
    for i in range(len(riadok)):
        riadok[i] = random.randint(0, 2)  # všetky prvky sú náhodné z <0, 2>
# t = [[random.randint(0, 2) for i in range(n)] for j in range(n)]]
kresli(t)
tkinter.mainloop()