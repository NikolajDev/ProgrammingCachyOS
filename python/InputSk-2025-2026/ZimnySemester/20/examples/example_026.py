obr1 = Image.open('tiger.bmp')
sirka, vyska = 150, 70
i = 0
for y in range(0, obr1.height, vyska):
    for x in range(0, obr1.width, sirka):
        obr1.crop((x, y, x+sirka, y+vyska)).save(f'tiger{i}.png')
        i += 1