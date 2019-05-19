class Solution(object):
    """
    Let N be the length of the string. 
    The middle of the palindrome could be in one of 
    2N - 1 positions: either at letter or between two letters.
    """
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        table = [[False for x in range(n)] for y in range(n)]
        count = 0

        # Every isolated char is a palindrome
        for i in range(n):
            table[i][i] = True
            count += 1

        # Check for a window of size 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        # Check windows of size 3 and more
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1

        return count

    def countSubstrings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        for center in range(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans