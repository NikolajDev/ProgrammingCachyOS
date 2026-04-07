>>> obd1 = Obdlznik(20, 7)
>>> print('obvod =', obd1.obvod())
    obvod = 54
>>> print(obd1)
    Obdlznik(20, 7)
>>> obd2 = obd1.kopia()
>>> obd2.zmen_velkost(2)
>>> print(obd2)
    Obdlznik(40, 14)