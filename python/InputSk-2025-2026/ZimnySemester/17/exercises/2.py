'''Dvojkový logaritmus môžeme počítať pomocou funkcie 
math.log2(cislo)
, ale vieme na to použiť aj algoritmus z prednášky, ktorý delením intervalu na polovice počítal druhú odmocninu. Napíš funkciu 
log2(cislo,
 
eps=0.001)
, ktorý to s nejakou presnosťou (parameter 
eps
) vypočíta takýmto algoritmom. Napríklad po spustení:


>>> 
log
(
1000
)


    9.965784382075071


>>> 
import
 
math


>>> 
math
.
log2
(
1000
)


    9.965784284662087






Otestuj pre rôzne hodnoty presnosti: 
0.1
, 
0.01
, 
0.001
, 
0.0001
, 
0.00001
.
'''