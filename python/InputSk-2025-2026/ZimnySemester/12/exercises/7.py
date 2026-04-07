'''-
 Zadefinuj triedu 
Stv
, ktorá zabezpečí definovanie farebného štvorčeka v grafickej ploche. Trieda bude mať tieto metódy:




metóda 
__init__(x,
 
y,
 
a=20,
 
farba='')
 vytvorí v grafickej ploche štvorček so stredom 
(x,
 
y)
, so stranou 
a
 a s výplňou 
farba
; ak má parameter 
farba
 hodnotu prázdny reťazec, tak sa nahradí vygenerovanou náhodnou farbou


metóda 
posun(dx,
 
dy)
 posunie objekt o 
(dx,
 
dy)


metóda 
zmen_farbu(farba)
 prefarbí štvorček na zadanú farbu




Okrem týchto metód definuj aj triedny atribút 
canvas
, ktorý bude spoločný pre všetky definované štvorčeky. Otestuj napríklad:


for
 
i
 
in
 
range
(
30
):

   
Stv
(
random
.
randint
(
50
,
 
300
),
 
random
.
randint
(
50
,
 
200
))






Otestuj aj posúvanie všetkých štvorčekov metódou 
posun
 aj prefarbovanie metódou 
zmen_farbu


Okrem triedy 
Stv
 zadefinuj aj triedu 
Dvojica
, pomocou ktorej sa budú vytvárať dvojice „zlepených“ štvorčekov (inštancií 
Stv
). Trieda bude mať tieto metódy:




metóda 
__init__(x,
 
y,
 
a=20)
 zadefinuje dva štvorčeky, pričom prvý z nich má stred v 
(x,
 
y)
 a druhý je k nemu prilepený sprava (má posunutý 
x
); oba majú veľkosť strán 
a
 a náhodné farby


metóda 
posun(dx,
 
dy)
 posunie oba štvorčeky o 
(dx,
 
dy)


metóda 
vymen()
 navzájom vymení farby oboch štvorčekov




Otestuj tak, že najprv vytvoríš 20 dvojíc na náhodných pozíciách s náhodnými veľkosťami z intervalu 
<20,
 
50>
. Potom ich všetky poposúvaj o nejaké 
(dx,
 
dy)
 a otestuj aj výmenu farieb v štvorčekoch.
'''