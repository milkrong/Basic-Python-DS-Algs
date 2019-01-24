class Solution(object):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
    """
    def max_sub_array(self, nums):
        if not nums:
            return None
        cur, res = nums[0], nums[0]
        for i in nums[1:]:
            cur = max(i, cur + i)
            res = max(cur, res)

        return res