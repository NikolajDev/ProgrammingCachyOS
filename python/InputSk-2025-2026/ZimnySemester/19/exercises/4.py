'''Odmeraj čas behu oboch algoritmov z (3). Použi 
time.time()
 a postupne meraj pre 
n
: 
10000
, 
20000
, 
40000
, 
80000
, 
160000
, …, 
5120000
. Asi bude vhodné pri meraní každé volanie vykonať viackrát, napríklad 
test1
 zavolaj 100 krát a 
test2
 10000 krát. Vypisované časy meraní by mali potvrdiť tvoj odhad zložitosti týchto funkcií. Môžeš využiť takúto schému merania času pomocou triedy 
Odmeraj
 a pythonovského príkazu 
with
:


import
 
time



class
 
Odmeraj
():


    
def
 
__enter__
(
self
):


        
self
.
t
 
=
 
time
.
time
()


    
def
 
__exit__
(
self
,
 
*
p
):


        
print
(
'odmerany cas'
,
 
round
(
time
.
time
()
-
self
.
t
,
 
4
))



def
 
sucet
(
n
):

    
res
 
=
 
0

    
for
 
i
 
in
 
range
(
1
,
 
n
+
1
):

        
res
 
+=
 
i

    
return
 
res



for
 
n
 
in
 
range
(
1000000
,
 
10000001
,
 
1000000
):

    
print
(
'pre n ='
,
 
n
,
 
'***'
,
 
end
=
' '
)


    
with
 
Odmeraj
():


        
sucet
(
n
)
'''