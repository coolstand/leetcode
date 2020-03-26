# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct(nums, 0, len(nums))

    def construct(self, nums, l, r):
        if l == r:
            return None
        
        pos = self.max(nums, l, r)
        cur = TreeNode(nums[pos])

        cur.left = self.construct(nums, l, pos)
        cur.right = self.construct(nums, pos+1, r)

        return cur

    def max(self, nums, l, r):
        pos = l
        for x in range(l,r):
            if nums[x] > nums[pos]:
                pos = x
        return pos