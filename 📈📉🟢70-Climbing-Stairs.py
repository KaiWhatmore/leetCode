def climbingStairs(n):
    a = 0
    b = 1
    total = 0
    for i in range(n):
        total = a + b
        a = b
        b = total

    return total
