'''Z prednášky vieme nakresliť 
Sierpińského trojuholník
 takto:


def
 
trojuholniky
(
n
,
 
a
):

    
if
 
n
 
>
 
0
:

        
for
 
i
 
in
 
range
(
3
):

            
t
.
fd
(
a
)

            
t
.
lt
(
120
)

            
trojuholniky
(
n
 
-
 
1
,
 
a
 
/
 
2
)



trojuholniky
(
4
,
 
300
)






Uprav túto rekurzívnu funkciu tak, aby všetky kreslené trojuholníky v 1. úrovni boli vyfarbené náhodnou farbou. Trojuholníky vo vyšších úrovniach nevyfarbuj. Táto kresba vyzerá ešte lepšie, keď sa bude kresliť so zdvihnutým perom.


Ďalej pridaj posúvač:


tkinter
.
Scale
(
orient
=
'horizontal'
,
 
from_
=
1
,
 
to
=
7
,
 
command
=
rob
)
.
pack
()






pomocou ktorého sa prekreslia trojuholníky už s novou úrovňou. Realizuj to podobne ako v 6. úlohe, v ktorej si urýchľoval vykresľovanie rekurzívneho obrázka pomocou dvojice 
turtle.tracer(0)
 a 
turtle.tracer(1)
.
'''