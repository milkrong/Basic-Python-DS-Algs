import math


def num_trees(n):
    """
    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
    :param n: int
    :return: int
    """
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            res[i] += res[j] * res[i - 1 - j]
    return res[n]


# Catalan Number  (2n)!/((n+1)!*n!)
def num_trees2(self, n):
    return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))