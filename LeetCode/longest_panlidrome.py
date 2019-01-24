class Solution(object):
    def longest_palidrome(self, s):
        res = ""
        for i in range(len(s)):
            tmp = self.find(i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.find(i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res


    def find(self, s, l, r):
        while l >=0 and r <= len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]