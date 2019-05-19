import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = []
        for x in nums:
            i = bisect.bisect_left(seq, x)
            if i == len(seq): seq.append(x)
            else: seq[i] = x
        return len(seq)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        dp = [1]
        for i in range(1, len(nums)):
            m = 0
            for j in range(0, i):
                if nums[j]<nums[i]:
                    if m<dp[j]:
                        m =  dp[j]
            dp.append(1+m) 
            
        return max(dp)