class Solution(object):
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        length = 1
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                nums[index + 1] = nums[i]
                length += 1
                index += 1
        return length
