def spir(d):
    pocet = 0
    while d <= 100:    # čo sa deje pred rekurzívnym volaním
        t.fd(d)
        t.lt(60)
        d += 3
        pocet += 1
    t.pencolor('red')  # triviálny prípad
    while pocet > 0:   # čo sa deje po vynáraní z rekurzie
        d -= 3
        t.fd(d)
        t.lt(60)
        pocet -= 1