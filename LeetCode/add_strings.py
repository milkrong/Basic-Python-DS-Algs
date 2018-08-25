def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    i = len(num1) - 1
    j = len(num2) - 1
    s = 0
    ans = ""
    while (s or i > -1 or j > -1):
        n1 = int(num1[i]) if i > -1 else 0
        n2 = int(num2[j]) if j > -1 else 0

        s = s + n1 + n2
        n = s % 10
        s = s / 10
        i -= 1
        j -= 1
        ans = str(n) + ans

    return ans