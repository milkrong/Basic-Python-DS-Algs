class Solution(object):
    def title_to_number(self, s):
        return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))