obr1 = Image.open('prasiatko.png')
obr2 = Image.open('masla.png')
obr2 = obr2.resize(2*i for i in obr2.size)
obr1.paste(obr2, (150, 100), obr2)