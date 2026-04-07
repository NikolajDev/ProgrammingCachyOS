if __name__ == '__main__':
    v = AritmetickyVyraz()
    print(f'{v.urob_prefix('1 2+') = }')
    print(f'{v.urob_prefix('abc') = }')
    print(f'{v.urob_prefix('-3*13 b') = }')
    print(f'{v.prirad('i', '24 j +') = }')
    print(f'{v.prirad('j', '2 3 4 5 ***') = }')
    print(v)
    print(f'{v.prirad('ij', 'i-j') = }')
    for prem in v.tab:
         print(prem, '=', v.vyhodnot(prem))
    print(v)