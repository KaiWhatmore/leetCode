cache = {}


def fib(n):
    if n in cache:
        return cache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)

    cache[n] = value
    return value


print(fib(5))
