'''-
 Funkcia 
kruh()
 z prednášky funguje aj bez určovania farby výplne:


def
 
kruh
(
r
,
 
x
,
 
y
,
 
**
param
):

    
canvas
.
create_oval
(
x
-
r
,
 
y
-
r
,
 
x
+
r
,
 
y
+
r
,
 
**
param
)






Doplň funkciu tak, aby každý takto kreslený kruh bol vyplnený buď farbou udanou v parametroch alebo bude inak červený, podobne, ak nie je daná hrúbka obrysu (
width
), nastaví sa hrúbka 3. Napríklad:


>>> 
kruh
(
100
,
 
100
,
 
100
,
 
outline
=
'blue'
,
 
width
=
1
)
    
# červený s hrúbkou 1


>>> 
kruh
(
30
,
 
50
,
 
100
,
 
fill
=
'blue'
)
                  
# modrý s hrúbkou 3
'''