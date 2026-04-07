body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
elif body >= 80:
    print('za', body, 'bodov získavaš známku B')
elif body >= 70:
    print('za', body, 'bodov získavaš známku C')
elif body >= 60:
    print('za', body, 'bodov získavaš známku D')
elif body >= 50:
    print('za', body, 'bodov získavaš známku E')
else:
    print('za', body, 'bodov si nevyhovel a máš známku Fx')