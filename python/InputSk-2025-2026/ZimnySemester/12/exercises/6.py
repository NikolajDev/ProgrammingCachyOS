'''odovzdaj
 Zadefinuj triedu, pomocou ktorej budeš vedieť reprezentovať obdĺžniky. Pri obdĺžnikoch nás budú zaujímať len veľkosti strán a na základe toho sa bude dať vypočítať ich obsah aj obvod. Dopíš všetky metódy:


class
 
Obdlznik
:

    
def
 
__init__
(
self
,
 
a
,
 
b
):

        
# inicializuje

        
...


    
def
 
__str__
(
self
):

        
# vráti reťazec v tvare 'Obdlznik(100, 70)'

        
...


    
def
 
obsah
(
self
):

        
# vráti obsah

        
...


    
def
 
obvod
(
self
):

        
# vráti obvod

        
...


    
def
 
zmen_velkost
(
self
,
 
pomer
):

        
# vynásobí obe veľkosti strán zadaným pomerom

        
...


    
def
 
kopia
(
self
):

        
# vyrobí kópiu samého seba

        
...






Otestuj, napríklad:


>>> 
obd1
 
=
 
Obdlznik
(
20
,
 
7
)


>>> 
print
(
'obvod ='
,
 
obd1
.
obvod
())


    obvod = 54


>>> 
print
(
obd1
)


    Obdlznik(20, 7)


>>> 
obd2
 
=
 
obd1
.
kopia
()


>>> 
obd2
.
zmen_velkost
(
2
)


>>> 
print
(
obd2
)


    Obdlznik(40, 14)
'''