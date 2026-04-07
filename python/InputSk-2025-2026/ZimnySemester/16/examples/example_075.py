class Fibonacci:
    def __getitem__(self, n):
        if n <= 1:
            return 1
        return self[n-1] + self[n-2]