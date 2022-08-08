cache = {}


def fib(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1
    elif n > 2:
        value = fib(n - 2) + fib(n - 1)
        cache[n] = value

    return value


print(fib(40))
