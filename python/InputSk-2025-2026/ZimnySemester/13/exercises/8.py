'''-
 Naprogramuj triedu 
Pero
, pomocou ktorej budeme vedieť kresliť do grafickej plochy. Trieda má tieto metódy:




__init__(x=0,
 
y=0)
, ak ešte nebola vytvorená grafická plocha (
canvas
 má hodnotu 
None
), vytvorí ju s danou šírkou a výškou, zapamätá si súradnice pera a stav, že pero je spustené dolu (bude kresliť)


pu()
 zdvihne pero, odteraz pohyb pera nekreslí


pd()
 spustí pero, pohyb bude zanechávať čiaru


setpos(x,
 
y)
 presunie pero na novú pozíciu, pritom, ak je pero spustené, zanecháva čiernu čiaru hrúbky 1




import
 
tkinter



class
 
Pero
:

    
canvas
 
=
 
None

    
sirka
,
 
vyska
 
=
 
400
,
 
300


    
def
 
__init__
(
...
):

        
...


    
def
 
pu
(
self
):

        
...


    
def
 
pd
(
self
):

        
...


    
def
 
setpos
(
self
,
 
x
,
 
y
):

        
...






Otestuj vytvorením dvoch inštancií pera, ktoré nakreslia napríklad dva štvorce:


p1
 
=
 
Pero
(
100
,
 
200
)


p2
 
=
 
Pero
(
200
,
 
150
)


...
'''