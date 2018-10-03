def integer_break(n):
    if n in [2,3]:
        return n - 1
    res = 1
    while n > 4:
        n = n-3
        res = res*3
    res = res*n

    return res