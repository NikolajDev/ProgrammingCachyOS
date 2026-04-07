def bin_retazec(n, k):
    if k == 0 or n == k:
        return '1'
    return bin_retazec(n - 1, k - 1) + '+' + bin_retazec(n - 1, k)

print(bin(6, 3), '=', bin_retazec(6, 3))