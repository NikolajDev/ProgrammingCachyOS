"""
odovzdaj Napíš funkciu vyhod_duplikaty(retazec), ktorá z daného reťazca vyhodí všetky za sebou idúce opakujúce sa znaky (nechá len jeden z nich). Napríklad:

"""

def vyhod_duplikaty(retazec):
    result = f"{retazec[0]}"
    last_ = retazec[0]
    for char in retazec:
        if char != last_:
            result += char
            last_ = char
    return result

x = vyhod_duplikaty("BBraatisssllavaaaaa")
print(x)