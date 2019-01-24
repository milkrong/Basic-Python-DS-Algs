class Solution(object):
    """
    Given a list of daily temperatures T, return a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature.
    If there is no future day for which this is possible,
    put 0 instead.
    """
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
          while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
          stack.append(i)

        return ans