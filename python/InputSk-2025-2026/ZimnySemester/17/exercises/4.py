'''Najjednoduchšia verzia asociatívneho poľa v prednáške:


class
 
AsocPole
:

    
def
 
__init__
(
self
):

        
self
.
tab
 
=
 
[]


    
def
 
__contains__
(
self
,
 
kluc
):

        
for
 
k
,
 
h
 
in
 
self
.
tab
:

            
if
 
k
 
==
 
kluc
:

                
return
 
True

        
return
 
False


    
def
 
__getitem__
(
self
,
 
kluc
):

        
for
 
k
,
 
h
 
in
 
self
.
tab
:

            
if
 
k
 
==
 
kluc
:

                
return
 
h

        
raise
 
KeyError


    
def
 
__setitem__
(
self
,
 
kluc
,
 
hodnota
):

        
for
 
i
,
 
(
k
,
 
h
)
 
in
 
enumerate
(
self
.
tab
):

            
if
 
k
 
==
 
kluc
:

                
self
.
tab
[
i
]
 
=
 
(
kluc
,
 
hodnota
)

                
return

        
self
.
tab
.
append
((
kluc
,
 
hodnota
))






Pomocou tejto implementácie slovníka napíš program, ktorý zo súboru 
skladatelia.txt
 zistí v ktorom roku sa narodilo najviac hudobných skladatelov. Zrejme najprv do slovníka 
AsocPole
 pre každý rok priradíš množinu všetkých skladatelľov s týmto rokom a potom pomocou štandardnej funkcie 
max
 vypíšeš rok s najväčšou množinou. Napríklad:


a
 
=
 
AsocPole
()


with
 
open
(
...
)
...

    
...


print
(
max
(
a
.
tab
,
 
...
))
   
# použi lambdu
'''