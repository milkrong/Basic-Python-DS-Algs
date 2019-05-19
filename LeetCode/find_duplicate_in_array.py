class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)-1
        while left < right:
           mid = (right + left)/2
           left, right = [left, mid] if sum(i <= mid for i in nums) > mid else [mid+1, right]
        return right