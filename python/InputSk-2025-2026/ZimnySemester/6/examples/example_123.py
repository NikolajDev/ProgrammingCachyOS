>>> t = open('subor.txt')
>>> print('prvý znak =', repr(t.read(1)))
>>> print('ďalších 10 znakov =', repr(t.read(10)))
>>> print('zvyšok súboru =', repr(t.read()))