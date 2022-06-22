from math import sqrt


def isPrime(n):
    if n == 1 or n == 0:
        return False

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
