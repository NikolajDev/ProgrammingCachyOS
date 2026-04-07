n = int(input('zadaj n: '))
for i in range(n):
    for j in range(n):
        print(f'{i*n + j + 1:2}', end=' ')
    print()