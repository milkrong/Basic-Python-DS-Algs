class Solution(object):
    def license_key_formatiing(self, S, K):
        """
        You are given a license key represented as a string S which consists only alphanumeric character and dashes. 
        The string is separated into N+1 groups by N dashes.
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]