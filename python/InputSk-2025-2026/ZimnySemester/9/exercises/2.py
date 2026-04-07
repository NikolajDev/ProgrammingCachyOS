'''-
 Napíš funkciu 
toint(retazec)
, ktorá prevedie daný reťazec na celé číslo. Môžeš predpokladať, že reťazec je neprázdny a obsahuje len desiatkové cifry. Funkcia nebude používať štandardnú funkciu 
int
 ale len funkciu 
ord()
.  Napíš túto funkciu najprv bez rekurzie pomocou while-cyklu, potom ju prepíš na rekurzívnu funkciu bez cyklu. Triviálnym prípadom by mohol byť jednoznakový vstupný reťazec (určite je to cifra). Rekurzívny prípad najprv prevedie celý reťazec ale bez posledného znaku na číslo, toto vynásobí 
10
 a pripočíta k tomu prevedený posledný znak reťazca. Funkcia nič nevypisuje. Napríklad:


>>> 
toint
(
'0'
)


    0


>>> 
toint
(
'17'
)


    17


>>> 
toint
(
'987654321'
)


    987654321
'''