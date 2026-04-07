>>> p1 = {'meno':'Janko Hrasko', 'vek':5, 'vyska':7, 'vaha':0.3, 'bydlisko':'Pri poli'}
>>> vypis(**p1)
    volam sa Janko Hrasko
         vaha = 0.3
         vek = 5
         vyska = 7
         bydlisko = Pri poli
>>> p2 = {'vek':25, 'narodeny':'Terchova', 'popraveny':'Liptovsky Mikulas'}
>>> vypis('Juraj Janosik', **p2)
    volam sa Juraj Janosik
         popraveny = Liptovsky Mikulas
         vek = 25
         narodeny = Terchova