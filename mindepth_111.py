# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def compare(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        m1 = self.compare(root.left)
        m2 = self.compare(root.right)
        if root.left is None or root.right is None:
            return m1+m2+1

        return min(m1, m2) + 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.compare(root)