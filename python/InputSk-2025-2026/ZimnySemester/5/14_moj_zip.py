"""
odovzdaj Python ponúka ešte jednu štandardnú funkciu zip. Táto funkcia, keď dostane nejaké dve postupnosti (napríklad zoznam, n-ticu, reťazec, range, …), vytvorí z nich jednu novú postupnosť dvojíc (tuple): v každej takejto dvojici je jeden prvok z prvej a jeden z druhej postupnosti. Môžeš vyskúšať, napríklad:

list(zip('python', [2, 3, 5, 7]))
    [('p', 2), ('y', 3), ('t', 5), ('h', 7)]
Zrejme, ak je jedna z týchto postupností kratšia, výsledok sa nastaví podľa nej. Napíš funkciu moj_zip(post1, post2), ktorá z dvoch postupností (iterovateľných objektov možno rôznej dĺžky) vytvorí jeden zoznam dvojíc. Samozrejme, že pritom nepoužiješ štandardnú funkciu zip().

"""

def moj_zip(post1, post2):
    result = []
    if len(post1) < len(post2):
        max_ = post2
        min_ = post1
    else:
        max_ = post1
        min_ = post2
    for i in range(len(min_)):
        result.append((post1[i], post2[i]))
    return result
    

print(moj_zip('python', [2, 3, 5, 7]))