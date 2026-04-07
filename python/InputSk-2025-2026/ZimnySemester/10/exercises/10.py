'''-
 Z prednášky uprav funkciu 
kresli
:


def
 
kresli
(
tab
,
 
d
=
20
,
 
farby
=
(
'black'
,
 
'yellow'
,
 
'orange'
,
 
'blue'
,
 
'red'
,
 
'white'
)):

    
canvas
.
delete
(
'all'
)

    
for
 
r
,
 
riadok
 
in
 
enumerate
(
tab
):

        
for
 
s
,
 
prvok
 
in
 
enumerate
(
riadok
):

            
x
,
 
y
 
=
 
s
 
*
 
d
 
+
 
5
,
 
r
 
*
 
d
 
+
 
5

            
farba
 
=
 
farby
[
prvok
]

            
canvas
.
create_rectangle
(
x
,
 
y
,
 
x
 
+
 
d
,
 
y
 
+
 
d
,

                                    
fill
=
farba
,
 
outline
=
'light gray'
)

    
canvas
.
update
()






tak, aby sa prvky tabuľky, ktoré majú hodnotu 
None
, nekreslili (ostalo po nich prázdne miesto). Teraz vytvor dvojrozmernú tabuľku 
p
 (všetky riadky majú rovnakú dĺžku 
5
), po vykreslení ktorej dostávaš takýto obrázok:
'''