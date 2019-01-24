class Solution(object):
    """
    Given an array of integers, find if the array contains any duplicates.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))