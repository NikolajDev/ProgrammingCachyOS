def spir(d):
    print(f'volanie spir({d})')
    if d > 100:
        pass     # nerob nič
        print('... trivialny pripad - nerobim nic')
    else:
        t.fd(d)
        t.lt(60)
        print(f'... rekurzivne volam spir({d + 3})')
        spir(d+3)
        print(f'... navrat z volania spir({d + 3})')

spir(92)