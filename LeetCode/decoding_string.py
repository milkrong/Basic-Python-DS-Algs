class Solution(object):
    """
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
    exactly k times. Note that k is guaranteed to be a positive integer.
    """
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += ch
        return stack[0][0]