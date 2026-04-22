'''
Napíš funkciu obdlznik(sirka, znak='*'), ktorá z daného znaku znak vypíše do troch riadkov výstupu obdĺžnik zadanej šírky. Napríklad pre volania:

obdlznik(30, '#')
obdlznik(6)
obdlznik(19, 'O')
dostaneme výstup:

##############################
#                            #
##############################
******
*    *
******
OOOOOOOOOOOOOOOOOOO
O                 O
OOOOOOOOOOOOOOOOOOO
'''


def obdlznik(sirka, znak="*"):
    print(f"{znak}" * sirka + "\n" + f"{znak}" + \
           " " * (sirka - 2) + f"{znak}\n" + f"{znak}" * sirka)

obdlznik(30, '#')
obdlznik(6)
obdlznik(19, 'O')