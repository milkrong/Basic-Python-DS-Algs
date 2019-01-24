class Solution(object):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

        #my bad solution
        # start, end, res = [0, 0, 0]
        # for index in range(1, len(prices)):
        #     if prices[index] < prices[index - 1]:
        #         start = prices[index]
        #     else:
        #         start = prices[index - 1]
        #         end = prices[index]
        #         res += end - start
        # return res