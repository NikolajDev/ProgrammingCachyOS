obr1 = Image.open('prasiatko.png')
obr2 = Image.open('masla.png')
obr3 = obr1.copy()
obr3.paste(obr2, (150, 100), obr2)
# obr1 ostal teraz nezmenený