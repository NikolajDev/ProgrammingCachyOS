def vypis(meno, **vlastnosti):
    print('volam sa', meno)
    for k, h in vlastnosti.items():
        print('    ', k, '=', h)