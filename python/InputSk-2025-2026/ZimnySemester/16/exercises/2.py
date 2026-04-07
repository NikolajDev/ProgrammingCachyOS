'''-
 Funkcia 
vykonaj()
 z prednášky spadne pri chybnom mene príkazu alebo chybnom parametri:


def
 
vykonaj
():

    
t
 
=
 
turtle
.
Turtle
()

    
p
 
=
 
{
'fd'
:
 
t
.
fd
,
 
'rt'
:
 
t
.
rt
,
 
'lt'
:
 
t
.
lt
}

    
while
 
True
:

        
prikaz
,
 
parameter
 
=
 
input
(
'> '
)
.
split
()

        
p
[
prikaz
](
int
(
parameter
))






Oprav ju tak, aby nespadla, ale vypísala sa o tom správa a ďalej sa pokračovalo. Využi metódu 
get()
 pre slovník, ktorá vyrieši situáciu so zle zadaným menom príkazu tak, že sa zavolá anonymná funkcia, ktorá vypíše správu (napríklad 
lambda:
 
print(f'chybne
 
meno
 
prikazu
 
{prikaz!r}'
). Napríklad:


 
>>>
 
vykonaj
()


     
>
 
fd
 
100


     
>
 
bk
 
50


     
chybne
 
meno
 
prikazu
 
'bk'


     
>
 
rt
 
90


     
>
 
lt
 
45
x


     
chybny
 
parameter
 
'45x'


     
>
'''