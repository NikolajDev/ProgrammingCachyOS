'''-
 Zadefinuj funkcie 
max2(tab)
, 
min2(tab)
, 
sum2(tab)
 a 
len2(tab)
, ktoré zistia (vrátia pomocou 
return
) najväčší prvok, najmenší prvok a súčet všetkých prvkov dvojrozmernej tabuľke 
čísel
 (bez prázdnych riadkov) a tiež počet prvkov tabuľky (teraz môže obsahovať prvky rôznych typov a aj prázdne riadky). Využi štandardné funkcie 
max()
, 
min()
, 
sum()
 a 
len()
. Všetky tieto funkcie zadefinuj pomocou generátorovej notácie, teda by mali byť v tvare:


def
 
max2
(
tab
):

    
return
 
...






Napríklad:


>>> 
p
 
=
 
[[
1
,
 
6
,
 
3.14
],
 
[
0.5
,
 
1.5
],
 
[
2.5
]]


>>> 
max2
(
p
)


    6


>>> 
min2
(
p
)


    0.5


>>> 
sum2
(
p
)


    14.64


>>> 
r
 
=
 
[[
-
1
,
 
-
2
],
 
[
-
3
,
 
-
4
]]


>>> 
max2
(
r
)


    -1


>>> 
min2
(
r
)


    -4


>>> 
len2
([[
1
,
 
2
,
 
3
],
 
[
2
],
 
[],
 
[
5
,
 
1
]])


    6
'''