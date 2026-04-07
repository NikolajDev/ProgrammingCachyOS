'''odovzdaj
 Napíš funkciu 
min_max(zoznam)
, ktorá pre neprázdny 
zoznam
 vráti (
return
) dvojicu hodnôt (najmenší, najväčší) prvok. Funkcia nepoužíva štandardné funkcie 
min
 a 
max
. Nepoužívaj globálne premenné. Riešenie bez rekurzie by mohlo vyzerať takto:


def
 
min_max
(
zoznam
):

    
minz
 
=
 
maxz
 
=
 
zoznam
[
0
]

    
for
 
p
 
in
 
zoznam
[
1
:]:

        
if
 
p
 
<
 
minz
:

            
minz
 
=
 
p

        
if
 
p
 
>
 
maxz
:

            
maxz
 
=
 
p

    
return
 
minz
,
 
maxz






Teraz to vyrieš rekurzívne bez cyklov.
'''