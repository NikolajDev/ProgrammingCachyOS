if __name__ == '__main__':
    ram = RAM('''
     const 0 4  # adresa, kde začína výsledné pole
     read 1     # n = input()
     read 2     # i = input()
     add 3 0    # pom = adresa začiatku poľa
     # adresa 4:
     store 3 2  # reg[pom] = i
     inc 2      # i += 1
     inc 3      # pom += 1
     dec 1      # n -= 1
     jnz 1 4    # if n != 0: jump 4
    ''')
    ram.start('12 250', 1)       # vstupná páska '12 250', počet bajtov pre registre je 1
    print(ram)