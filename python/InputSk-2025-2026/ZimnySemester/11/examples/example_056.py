z = set()                  # prázdna pythonovská množina
z.add('behat')
z.add('upratat')
z.add('ucit sa')
if 'behat' in z:
    print('musis behat')
else:
    print('nebehaj')
z.add('upratat')
print('zoznam =', z)
z.discard('spievat')
print('pocet prvkov v zozname =', len(z))