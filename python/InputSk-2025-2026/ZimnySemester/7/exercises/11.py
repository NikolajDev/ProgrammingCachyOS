'''-
 Napíš program, ktorý bude robiť efekt spreja: ťahanie myšou so zatlačeným ľavým tlačidlom nakreslí 20 farebných bodiek (farba podľa globálnej premennej, napríklad 
farba
 
=
 
'blue'
) na náhodných pozíciách. Tieto náhodné bodky budú mať od kliknutého miesta takúto vzdialenosť: x-ová súradnica bude z intervalu 
<x-30,
 
x+30>
 a y-ová z 
<y-30,
 
y+30>
. Najlepšie je ich kresliť ako kruhy s polomerom 
2
 bez obrysu (
width=0
).


Do programu pridaj aj spracovanie tlačidla 
'Zmeň
 
farbu'
: vtedy sa nastaví premenná 
farba
 na náhodnú farbu. Vďaka tomuto každé ďalšie ťahanie myšou bude sprejovať už touto novou farbou. Okrem tlačidla pridaj aj widget 
Label
, ktorý bude zobrazovať aktuálne nastavenú farbu spreja, napríklad v tvare: 
'farba:
 
#456789'
. Môžeš použiť napríklad:


vypis
 
=
 
tkinter
.
Label
(
text
=
'farba: blue'
)


vypis
.
pack
()






a pre zmenu textu v tomto widgete:


vypis
[
'text'
]
 
=
 
'novy text'
'''