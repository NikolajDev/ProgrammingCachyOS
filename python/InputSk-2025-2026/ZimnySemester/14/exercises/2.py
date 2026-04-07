'''Prepíš tento výraz:


(
3
 
+
 
4
)
 
*
 
5
 
+
 
2
 
**
 
(
100
 
//
 
5
)






tak, aby si všetky operácie nahradil magickými metódami. Potom skontroluj, či jeho vykonaním dostaneš rovnaký výsledok:


>>> 
(
3
 
+
 
4
)
 
*
 
5
 
+
 
2
 
**
 
(
100
 
//
 
5
)


    1048611


>>> 
(
3
)
.
__add__
(
4
)
...






Ďalej prepíš nasledovný výraz teraz bez magických funkcii a opäť skontroluj:


>>> 
(
7
)
.
__pow__
(
8
)
.
__str__
()
.
__len__
()
.
__add__
(
'xy'
.
__rmul__
(
8
)
.
__len__
()
.
__add__
(
1
))
.
__mul__
(
13
)


    312


>>> 
...
 
7
 
**
 
8
 
...
'''