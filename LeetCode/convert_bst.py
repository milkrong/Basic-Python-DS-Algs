# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        Given a Binary Search Tree (BST), convert it
        Tree such that every key of the original BST is changed 
        to the original key plus sum of all keys greater than the original key in BST.
        :type root: TreeNode
        :rtype: TreeNode
        """
        s = []
        p = root
        while p:
            s.append(p)
            p = p.right
        
        total = 0
        while s:
            cur = s.pop()
            total += cur.val
            cur.val = total
            cur = cur.left
            while cur:
                s.append(cur)
                cur = cur.right
        return root