class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt +=1
                res = max(cnt, res)
            else:
                cnt = 0
                
        return res
        