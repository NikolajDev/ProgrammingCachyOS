'''-
 Ručne bez počítača zisti, čo sa bude vypisovať (funkcia 
vymen(zoz,
 
i,
 
j)
 vymení obsahy 
i
-teho a 
j
-teho prvku daného zoznamu 
zoz
):


bublinkové triedenie


def
 
bubble_sort
(
zoz
):

    
for
 
i
 
in
 
range
(
len
(
zoz
)):

        
for
 
j
 
in
 
range
(
len
(
zoz
)
-
1
):

            
if
 
zoz
[
j
]
 
>
 
zoz
[
j
+
1
]:

                
vymen
(
zoz
,
 
j
,
 
j
+
1
)


        
print
(
*
zoz
)




z
 
=
 
[
13
,
 
7
,
 
11
,
 
3
,
 
5
,
 
2
]


bubble_sort
(
z
)






triedenie s výberom minimálneho prvku


def
 
min_sort
(
zoz
):

    
for
 
i
 
in
 
range
(
len
(
zoz
)
-
1
):

        
for
 
j
 
in
 
range
(
i
+
1
,
 
len
(
zoz
)):

            
if
 
zoz
[
i
]
 
>
 
zoz
[
j
]:

                
vymen
(
zoz
,
 
i
,
 
j
)


        
print
(
*
zoz
)




z
 
=
 
[
13
,
 
7
,
 
11
,
 
3
,
 
5
,
 
2
]


min_sort
(
z
)






triedenie vkladaním


def
 
insert_sort
(
zoz
):

    
for
 
i
 
in
 
range
(
1
,
 
len
(
zoz
)):

        
j
 
=
 
i

        
while
 
j
 
>
 
0
 
and
 
zoz
[
j
-
1
]
 
>
 
zoz
[
j
]:

            
vymen
(
zoz
,
 
j
-
1
,
 
j
)

            
j
 
-=
 
1


        
print
(
*
zoz
)




z
 
=
 
[
13
,
 
7
,
 
11
,
 
3
,
 
5
,
 
2
]


insert_sort
(
z
)
'''