def factorial(n):
    if n == 1:
        return 1

    print(n)
    return n * factorial(n - 1)


factorial(5)
