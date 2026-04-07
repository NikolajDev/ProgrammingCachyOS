body = int(input('Zadaj získaný počet bodov: '))
hranica = 90
for znamka in 'ABCDEF':
    if body >= hranica:
        break
    hranica -= 10

if znamka != 'F':
    print('za', body, 'bodov získavaš známku', znamka)
else:
    print('za', body, 'bodov si nevyhovel a máš známku Fx')