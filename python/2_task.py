def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    premena = factorial(5)
    assert premena == 120


if __name__ == "__main__":
    main()
