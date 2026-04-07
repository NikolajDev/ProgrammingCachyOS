subor = open('meno súboru', 'r')

riadok = subor.readline()
while riadok != '':
    # ... spracuj riadok
    riadok = subor.readline()

subor.close()