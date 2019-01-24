class Solution(object):
    """
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    """
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            if dic[num] > len(nums)//2:
                return num
            else:
                dic[num] += 1

    def majority_element2(self, num):
        return sorted(num)[len(num) / 2]

