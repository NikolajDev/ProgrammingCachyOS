obr1 = Image.open('prasiatko.png')
obr2 = Image.open('macka.png').convert('RGBA').rotate(30, expand=True)
obr1.paste(obr2, (150, 100), obr2)