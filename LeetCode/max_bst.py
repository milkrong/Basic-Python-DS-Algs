# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    root is max in array, and left right sub tree is sep by the max val
    """
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])
        node.left = self.constructMaximumBinaryTree(nums[:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid + 1:])
        return node