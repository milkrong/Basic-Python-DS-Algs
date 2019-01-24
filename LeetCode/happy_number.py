class Solution(object):
    """
    A happy number is a number defined by the following process: Starting with any positive integer,
    replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
    (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy numbers.
    """

    def is_happy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check_list = set()
        while n != 1:
            n = sum([int(e) ** 2 for e in str(n)])
            if n in check_list:
                return False
            else:
                check_list.add(n)
        else:
            return True


s = Solution()
print(s.is_happy(19))