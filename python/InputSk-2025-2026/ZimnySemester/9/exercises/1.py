'''-
 Napíš funkciu 
tostr(cislo)
, ktorá pomocou štandardnej funkcie 
chr()
 (bez konverzie 
str()
) prevedie dané nezáporné celé číslo na znakový reťazec. Napíš túto funkciu najprv bez rekurzie pomocou while-cyklu, potom ju prepíš na rekurzívnu funkciu bez cyklu. Triviálnym prípadom by mohlo byť jednociferné celé číslo. Rekurzívny prípad najprv prevedie na reťazec číslo bez poslednej cifry a potom k nemu prireťazí poslednú cifru. Funkcia nič nevypisuje. Napríklad:


>>> 
tostr
(
0
)


    '0'


>>> 
tostr
(
17
)


    '17'


>>> 
tostr
(
987654321
)


    '987654321'
'''