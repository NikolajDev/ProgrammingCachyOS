'''Napíš rekurzívnu funkciu 
dva_sucty(zoznam)
, ktorá bez cyklov zistí súčet záporných prvkov zoznamu a súčet kladných prvkov zoznamu (ľubovoľnej postupnosti čísel). Funkcia vráti dvojicu (
tuple
) týchto dvoch súčtov. Riešenie si premysli tak, aby funkcia prešla prvkami vstupného zoznamu len raz. Otestuj, napríklad:


>>> 
dva_sucty
(
range
(
-
5
,
 
7
))


    (-15, 21)


>>> 
dva_sucty
((
0
,
 
1
,
 
-
2
,
 
3
,
 
4
,
 
-
5
,
 
-
6
,
 
7
))


    (-13, 15)


>>> 
dva_sucty
(
list
(
range
(
100
))
 
+
 
list
(
range
(
0
,
 
-
100
,
 
-
1
)))


    (-4950, 4950)


>>> 
dva_sucty
([
0
]
*
1000
+
[
1
]
+
[
0
]
*
1000
+
[
-
1
]
+
[
0
]
*
1000
)


    (-1, 1)
'''