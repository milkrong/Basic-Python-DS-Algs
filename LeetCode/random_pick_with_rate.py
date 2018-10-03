import random


class Solution:
    """
    Given an array w of positive integers, where w[i] describes the weight of index i,
    write a function pickIndex which randomly picks an index in proportion to its weight.
    """

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.n = len(w)
        self.s = sum(self.w)
        for i in range(1, self.n):
            w[i] += w[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(1, self.s)
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l