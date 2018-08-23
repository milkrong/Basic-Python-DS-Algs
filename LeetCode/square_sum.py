from math import sqrt

def square_sum(c):

    i, j = 0, int(sqrt(c))
    while i <= j:
        pow_sum = i*i + j*j
        if pow_sum == c:
            return True
        elif pow_sum > c:
            j -= 1
        else:
            i += 1

    return False

print(square_sum(5))
