>>> generuj('F', ['F -> F-F++F-F'], 2)
    'F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F'
>>> for pocet in range(4):
...     print(pocet, repr(generuj('a', ('a->Fb[-a]+a', 'b->Fb'), pocet)))
    0 'a'
    1 'Fb[-a]+a'
    2 'FFb[-Fb[-a]+a]+Fb[-a]+a'
    3 'FFFb[-FFb[-Fb[-a]+a]+Fb[-a]+a]+FFb[-Fb[-a]+a]+Fb[-a]+a'