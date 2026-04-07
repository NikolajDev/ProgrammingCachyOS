teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = sum(teploty)
maximum = max(teploty)
minimum = min(teploty)
priemer = sucet / len(teploty)
print('priemerná teplota je', f'{priemer:.1f}')
print('minimálna teplota je', minimum)
print('maximálna teplota je', maximum)