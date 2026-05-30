"""
Napíš funkciu ozatvorkuj(retazec, podretazec), ktorá v zadanom reťazci retazec ozátvorkuje všetky výskyty daného podreťazca. Napríklad:

b = ozatvorkuj('Bratislava', 'a')
b
    'Br(a)tisl(a)v(a)'
ozatvorkuj('prospešné programovanie v prologu', 'pro')
    '(pro)spešné (pro)gramovanie v (pro)logu'

"""

def ozatvorkuj(retazec, podretazec):
    return retazec.replace(podretazec, f"({podretazec})")

if __name__ == "__main__":
    print(ozatvorkuj('prospešné programovanie v prologu', 'pro'))