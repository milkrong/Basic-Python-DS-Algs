class Solution(object):
    """
    You are given coins of different denominations and a total amount of money amount.
    Write a function to compute the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        stack = [(0, 0, len(coins))] # steps, accumulated
        min_steps = 2**31
        while len(stack) != 0:
            steps, accumulated, sequence = stack.pop()
            if accumulated == amount:
                min_steps = min(min_steps, steps)
            if accumulated > amount or amount - accumulated > coins[sequence-1] * (min_steps-steps):
                continue
            for seq, coin in enumerate(coins[:sequence]):
                stack.append((steps+1, accumulated+coin, seq+1))
        return min_steps if min_steps != 2**31 else -1

coins = [1,2,5] 
amount = 11
s = Solution()
res = s.coinChange(coins, amount)
print(res)