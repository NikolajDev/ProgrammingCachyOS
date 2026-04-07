to lupen :d [repeat 2[repeat 6[fd :d rt 15] rt 90]]
to koment :text []
to kvet :n :d[
    koment 'nakresli kvet'
    repeat :n[lupen :d rt 360/:n]]
kvet 7 10 pu
repeat 9[fd 200 pd kvet 7 10 pu fd -200 lt 80]