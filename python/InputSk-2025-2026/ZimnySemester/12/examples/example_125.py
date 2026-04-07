g = MojaGrafika()
g.stvorec(280, 200, 150, 'yellow')
for x in range(20, 400, 40):
    g.kruh(20, x, 100)               # náhodné farby
g.text('Python', 200, 150, 'red')
g.zapis('grafika.txt')               # vytvorí súbor