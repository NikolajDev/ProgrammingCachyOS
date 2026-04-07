'''Program počas ťahania myši zabezpečí kreslenie žltých krúžkov, prvý s polomerom 
1
, každý ďalší je o 
0.1
 väčší. Tlačidlom 
'Zmaž'
 sa obrazovka zmaže a nastaví sa kreslenie od najmenšieho krúžku (s polomerom 
1
). V programe zabezpeč zviazanie ovládača a tlačidla:


canvas
.
bind
(
'<B1-Motion>'
,
 
kresli
)


tkinter
.
Button
(
...






Po spustení a ťahaní môžeš dostať, napríklad:






Teraz pridaj ďalšie tlačidlo (napríklad s textom 
'Zmeň
 
farbu'
), ktorým sa zmení farba krúžkov na nejakú náhodnú - od tohto momentu budú všetky nasledovné krúžky zafarbené touto novou farbou.
'''