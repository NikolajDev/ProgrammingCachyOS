"""
Možno poznáš pesničk{char} '{char}ed{char}
 mucha na stene, sedí a spí.'. Napíš program, ktorý si najprv vypýta zoznam nejakých samohlások a potom pre každú z nich vypíše túto vetu tak, že v nej všetky samohlásky nahradí touto konkrétnou. Zrejme využiješ for-cyklus a formátovací reťazec f'S{i}d{i} m{i}ch{i} ...'. Môžeš dostať takýto výstup:

zadaj samohlásky: eaôiuý
Sede meche ne stene, sede e spe.
Sada macha na stana, sada a spa.
Sôdô môchô nô stônô, sôdô ô spô.
Sidi michi ni stini, sidi i spi.
Sudu muchu nu stunu, sudu u spu.
Sýdý mýchý ný stýný, sýdý ý spý.

"""

vowels = input("Enter vowels: ")
for char in vowels:
    print(f"""S{char}d{char} m{char}ch{char} n{char}
     st{char}n{char}, s{char}d{char} {char} sp{char}.""")