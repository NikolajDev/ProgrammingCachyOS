>>> tel = {'Betka':737373, 'Dusan':555444, 'Anka': 363636, 'Egon':210210,
    'Cyril': 911111, 'Gaba':123456, 'Fero':288288}
>>> sorted(tel.items())
    [('Anka', 363636), ('Betka', 737373), ('Cyril', 911111), ('Dusan', 555444),
     ('Egon', 210210), ('Fero', 288288), ('Gaba', 123456)]
>>> sorted(tel.items(), key=lambda x: x[1])
    [('Gaba', 123456), ('Egon', 210210), ('Fero', 288288), ('Anka', 363636),
     ('Dusan', 555444), ('Betka', 737373), ('Cyril', 911111)]