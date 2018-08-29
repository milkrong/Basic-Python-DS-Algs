def three_sum(nums):
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    :param nums: list[int]
    :return: list[list[int]]
    """
    if len(nums) < 3:
        return []

    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1;
                r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res