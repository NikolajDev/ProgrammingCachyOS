'''-
 Do funkcie 
strom
, pomocou ktorej korytnačka nakreslí binárny strom, dopíš kreslenie farebných bodiek na koncoch všetkých vetvičiek (napríklad pomocou 
t.dot(10,
 
farba)
). Farbu každej bodky postupne (cyklicky) vyberaj zo zoznamu farieb 
zoznam
:


zoznam
 
=
 
[
'red'
,
 
'blue'
,
 
'gold'
,
 
'green'
]



def
 
strom
(
d
):

    
t
.
fd
(
d
)

    
if
 
d
 
>
 
10
:

        
t
.
lt
(
40
)

        
strom
(
d
 
*
 
0.7
)

        
t
.
rt
(
75
)

        
strom
(
d
 
*
 
0.6
)

        
t
.
lt
(
35
)

    
t
.
bk
(
d
)



t
.
lt
(
90
)


t
.
pu
()


t
.
fd
(
-
200
)


t
.
pd
()


strom
(
100
)






Aby toto fungovalo aj s použitím posúvača (vtedy pri každom posune zmaže doterajšiu kresbu a nakreslí ju s novým parametrom 
d
):


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
10
,
 
to
=
200
,
 
command
=
rob
)
.
pack
()






bude treba maximálne urýchliť kreslenie stromu vo funkcii 
rob
. Tiež si uvedom, že táto funkcia musí mať jeden formálny parameter, v ktorom nám systém vráti momentálnu hodnotu bežca posúvača (ako reťazec). Na urýchlenie kreslenia stromu môžeš na začiatku funkcie 
rob
 vložiť 
turtle.tracer(0)
 a na koniec 
turtle.tracer(1)
. Program by mal správne fungovať pre 
zoznam
 s ľubovoľným počtom farieb.
'''