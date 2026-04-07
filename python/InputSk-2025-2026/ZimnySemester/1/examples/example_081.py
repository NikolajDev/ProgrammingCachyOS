pocet = 0
suma = 0
for cena in 1.75, 2.20, 1.03, 4.00, 3.50, 2.90, 1.89:
    suma = suma + cena
    pocet = pocet + 1
print('nakúpil si', pocet, 'položiek')
print('za', suma, 'euro')
print('priemerná cena bola', round(suma / pocet, 2), 'euro')