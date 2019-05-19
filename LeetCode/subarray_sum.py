class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        res = pre_sum = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res